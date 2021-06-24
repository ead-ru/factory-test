from django.db import models
from django.conf import settings


class Poll(models.Model):
    ''' '''

    title = models.CharField(max_length=255)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    descr = models.TextField()

    def __str__(self):
        ''' '''
        return self.title


class Question(models.Model):
    ''' '''

    TYPE_TEXT = 'text'
    TYPE_SELECT = 'select'
    TYPE_MULTISELECT = 'multiselect'
    TYPES = [(TYPE_TEXT, 'Text'), (TYPE_SELECT, 'Select'), (TYPE_MULTISELECT, 'Multiselect')]

    text = models.TextField()
    type = models.CharField(max_length=15, choices=TYPES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        ''' '''
        return self.text


class QuestionChoice(models.Model):
    ''' '''

    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        ''' '''
        return self.text


class UserPoll(models.Model):
    ''' '''

    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Answer(models.Model):
    ''' '''

    user_poll = models.ForeignKey(UserPoll, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, blank=True, null=True)
