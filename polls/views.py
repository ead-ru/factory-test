from django.utils import timezone
from rest_framework import viewsets, permissions, mixins, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from polls import models
from polls import serializers


class PollViewSet(viewsets.ModelViewSet):
    ''' '''

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

    def get_permissions(self):
        ''' '''
        if self.action == 'active':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def active(self, request):
        ''' '''
        polls = models.Poll.objects.filter(end_dt__gt=timezone.now())
        serializer = self.get_serializer(polls, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    ''' '''

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionChoiceViewSet(viewsets.ModelViewSet):
    ''' '''

    queryset = models.QuestionChoice.objects.all()
    serializer_class = serializers.QuestionChoiceSerializer
    permission_classes = [permissions.IsAdminUser]


class UserPollViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    ''' '''
    serializer_class = serializers.UserPollSerializer
    _user_id = None

    def list(self, request, *args, **kwargs):
        ''' '''
        self._user_id = request.GET.get('uid', None) if request.user.is_anonymous else request.user.id
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        ''' '''
        if self._user_id:
            return models.UserPoll.objects.filter(user_id=self._user_id)
        else:
            return []


class AnswersViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    ''' '''

    serializer_class = serializers.AnswerSerializer

