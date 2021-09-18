# from django.contrib.auth.models import User, Group
from quest.models import quest, author, sample
from rest_framework import serializers

class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = quest.Quest
        fields = "__all__"
