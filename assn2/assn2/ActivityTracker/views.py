from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Activity, TimeLog
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    activities = Activity.objects.all()
    return render(request, "ActivityTracker/index.html", {"activities": activities})

def newActivity(request):
    return render(request, "ActivityTracker/newActivity.html")

def logNewActivity(request):
    params = request.POST
    if params.get("content") == "":
        return redirect("/")
    newActivity = Activity(
        name=params.get("content").title()
    )
    newActivity.save()
    return redirect("/")

def timeLog(request, id):
    activity = Activity.objects.get(id=id)
    timeLogs = TimeLog.objects.filter(activity_id=id)
    return render(request, "ActivityTracker/timeLog.html", {"activity": activity, "timeLogs": timeLogs})

def addTimeLog(request, id):
    activity = Activity.objects.get(id=id)
    return render(request, "ActivityTracker/newTimeLog.html")

def logNewTimeLog(request, id):
    params = request.POST
    if params.get("startDatetime") == "" or params.get("endDatetime") == "":
        return redirect(f"/activity/{id}")
    startTime = datetime.strptime(params.get("startDatetime"), '%Y-%m-%dT%H:%M')
    endTime = datetime.strptime(params.get("endDatetime"), '%Y-%m-%dT%H:%M')
    delta = timedelta()
    delta += (endTime - startTime)
    timeLog = TimeLog(
        startTime = startTime,
        endTime = endTime,
        timeSpent = str(delta),
        activity = Activity.objects.get(id=id)
    )
    timeLog.save()
    return redirect(f"/activity/{id}")

def deleteActivity(request, id):
    activity = Activity.objects.get(id=id)
    activity.delete()
    return redirect("/")
