from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import QuestionViewSet,AnswerViewSet
# ,UserViewSet



router = routers.DefaultRouter()
router.register('question',QuestionViewSet)
router.register('answer',AnswerViewSet)
# router.register('users',UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]
