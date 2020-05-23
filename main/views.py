from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer,AnswerSerializer
from rest_framework import generics



class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer
