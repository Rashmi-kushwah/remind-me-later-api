
# reminder/models.py
from django.db import models

class Reminder(models.Model):
    REMIND_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    remind_type = models.CharField(max_length=10, choices=REMIND_CHOICES)

    def __str__(self):
        return f"{self.message} at {self.date} {self.time} via {self.remind_type}"
