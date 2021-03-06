from django.db import models
from datetime import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return str(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, unique=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
