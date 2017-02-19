from django.shortcuts import (render, get_object_or_404)
from django.http import (HttpResponse, HttpResponseRedirect, Http404)
from django.urls import (reverse, reverse_lazy)
from django.db.models import (ExpressionWrapper, F, DateTimeField)
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Choice, Question
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache
# from .mixins import LoginRequiredMixin
from extras.fbv_to_cbv_decorator import class_view_decorator1, class_view_decorator2

from .forms import QuestionForm

decorators = [login_required, never_cache]


#-------------------------------------------------------------------------

# class IndexView(LoginRequiredMixin, generic.ListView):

#@method_decorator(login_required, name='dispatch')

#@class_view_decorator2(login_required)
#@class_view_decorator1(login_required)
@method_decorator(decorators, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # default context variable provided by django here would be question_list
    # default context name is 'object_list'
    context_object_name = 'latest_que_list'

    def head(self, *args, **kwargs):
        latest_question = self.get_queryset()[0]
        # or self.get_queryset().latest('question_text') or use reverse() if
        # ordering is used
        response = HttpResponse('')
        response['Last - Modified'] = latest_question.pub_date.strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        return response

    def get_queryset(self):
        return Question.objects.all()

    #@method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #    return super(IndexView, self).dispatch(*args, **kwargs)

        # can also over ride the get_context_data() method here
    # context = {
    #    'latest_que_list': Question.objects.order_by('-pub_date'),
    #}
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse(', '.join([q.question_text for q in
        # latest_que_list[:5]]))

#-------------------------------------------------------------------------


# FormView wxample for adding question
# class QuestionView(generic.edit.FormView):
#     template_name = "polls/question.html"
#     form_class = QuestionForm
#     success_url = "/polls/"

#     def is_valid(self):
#         return super(QustionView, self).is_valid()

#     def form_valid(self, form):
#         data = form.cleaned_data
#         Question(question_text=data['question_text'],
#                  pub_date=data['pub_date']).save()
        #         return super(QuestionView, self).form_valid(form)


class QuestionView(generic.edit.CreateView):
    model = Question
    template_name = 'polls/question.html'
    fields = '__all__'
    success_url = reverse_lazy('polls:index')
    #success_url = '/polls/'


#-------------------------------------------------------------------------


class QuestionEditView(generic.edit.UpdateView):
    model = Question
    template_name = 'polls/question.html'
    #template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/polls/'

#--------------------------------------------------------------------------


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['boom'] = 'AJ'
        return context
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
