from django import forms
from .models import Question
from datetime import datetime


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    pub_date = forms.DateTimeField()
