from django.db import models
from datetime import timedelta

class Activity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    def time_spent(self):
        delta = timedelta()
        for timelog in self.timeLogs.all():
            delta += (timelog.endTime - timelog.startTime)
        return str(delta)

class TimeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    timeSpent = models.TextField()
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name="timeLogs")

