from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (CreateView, DeleteView)
from django.core.urlresolvers import reverse_lazy

from . import views
from .models import Question


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^polls/question/$', views.QuestionView.as_view(), name='question'),
    url(r'^polls/question/$', CreateView.as_view(model=Question, template_name='polls/question.html',
                                                 fields='__all__', success_url=reverse_lazy('polls:index')), name='question'),
    url(r'^polls/question/(?P<pk>[0-9]+)/$',
        views.DetailView.as_view(), name='detail'),
    url(r'^polls/question/(?P<pk>[0-9]+)/edit/$',
        views.QuestionEditView.as_view(), name='update'),
    url(r'^polls/question/(?P<pk>[0-9]+)/delete/$',
        DeleteView.as_view(model=Question, success_url=reverse_lazy('polls:index')), name='delete'),
    url(r'^polls/question/(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(), name='results'),
    url(r'^polls/question/(?P<question_id>[0-9]+)/vote',
        views.vote, name='vote'),
]
