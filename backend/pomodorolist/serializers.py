from rest_framework import serializers
from .models import PomodoroList

class PomodoroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroList
        fields = ('id','title','description','completed')