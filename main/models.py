from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=50)


class Answer(models.Model):
    answer = models.CharField(max_length=50)
