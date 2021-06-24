from rest_framework import serializers
from polls import models


class QuestionChoiceSerializer(serializers.ModelSerializer):
    ''' '''

    class Meta:
        model = models.QuestionChoice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    ''' '''

    choices = QuestionChoiceSerializer(many=True, required=False)

    class Meta:
        model = models.Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    ''' '''

    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = models.Poll
        fields = '__all__'

    def update(self, instance, validated_data):
        ''' @todo? '''
        validated_data['start_dt'] = instance.start_dt
        return super().update(instance, validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    ''' '''

    class Meta:
        model = models.Answer
        fields = '__all__'


class UserPollSerializer(serializers.ModelSerializer):
    ''' '''

    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = models.UserPoll
        fields = '__all__'

    def create(self, validated_data):
        ''' '''
        request = self.context.get('request')
        if request and hasattr(request, 'user') and not request.user.is_anonymous:
            validated_data['user_id'] = request.user.id
        return super().create(validated_data)
