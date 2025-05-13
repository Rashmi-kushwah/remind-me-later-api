from django.shortcuts import render

# Create your views here.
# reminder/views.py
from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderCreateView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
