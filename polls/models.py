from django.db import models
from rest_framework import serializers


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

    def need_choices(self) -> bool:
        ''' '''
        return not (self.type == self.TYPE_TEXT)


class QuestionChoice(models.Model):
    ''' '''

    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        ''' '''
        return self.text

    def save(self, force_insert=False, force_update=False, using=None,
            update_fields=None):
        ''' '''
        if not self.question.need_choices():
            raise serializers.ValidationError('This type of question does not need choices')
        super().save(force_insert, force_update, using, update_fields)


class UserPollManager(models.Manager):
    ''' '''

    def check_if_owner(self, poll_id: int, user_id: int) -> bool:
        ''' '''
        return self.filter(user_id=user_id, poll_id=poll_id).exists()


class UserPoll(models.Model):
    ''' '''

    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    objects = UserPollManager()


class Answer(models.Model):
    ''' '''

    user_poll = models.ForeignKey(UserPoll, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
            update_fields=None):
        ''' '''
        if self.question.need_choices():
            if not self.chosen or not self.question.choices.filter(id=self.chosen_id).exists():
                raise serializers.ValidationError('Choose your answer from provided choices')
            self.text = None
        else:
            if self.chosen and not self.text:
                raise serializers.ValidationError('This answer does not need choices')
            self.chosen = None
        super().save(force_insert, force_update, using, update_fields)
