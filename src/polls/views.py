from django.shortcuts import (render, get_object_or_404)
from django.http import (HttpResponse, HttpResponseRedirect, Http404)
from django.urls import reverse
from django.db.models import (ExpressionWrapper, F, DateTimeField)
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Choice, Question
from django.contrib.auth.mixins import LoginRequiredMixin
# from .mixins import LoginRequiredMixin
from extras.fbv_to_cbv_decorator import class_view_decorator


# class IndexView(LoginRequiredMixin, generic.ListView):
#@method_decorator(login_required, name='dispatch')
@class_view_decorator(login_required)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # default context variable provided by django here would be question_list
    context_object_name = 'latest_que_list'

    def get_queryset(self):
        return Question.objects.all()

    #@method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #    return super(IndexView, self).dispatch(*args, **kwargs)

    # context = {
        #    'latest_que_list': Question.objects.order_by('-pub_date'),
        #}
        # return render(request, 'polls/index.html', context)
        # return HttpResponse(template.render(context, request))
        # return HttpResponse(', '.join([q.question_text for q in
        # latest_que_list[:5]]))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    #question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    #question = get_object_or_404(Question, pk=question_id)
    #today_date = ExpressionWrapper(F('pub_date'), output_field=DateTimeField())
    # return render(request, 'polls/results.html', {'question': question,
    # 'date': today_date})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error': "You didn't select a choice.",
        })
    selected_choice.votes = F('votes') + 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
