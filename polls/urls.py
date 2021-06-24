from django.urls import path, include
from rest_framework import routers
from polls import views


router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'questions-choices', views.QuestionChoiceViewSet)
router.register(r'users', views.UserPollViewSet, basename='users')
router.register(r'answers', views.AnswersViewSet, basename='answers')


app_name = 'polls'
urlpatterns = router.urls
