from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PomodoroListSerializer
from .models import PomodoroList

class PomodoroListView(viewsets.ModelViewSet):
    serializer_class = PomodoroListSerializer
    queryset = PomodoroList.objects.all()

# Create your views here.
