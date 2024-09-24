from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newActivity/", views.newActivity, name="New Activity"),
    path("logNewActivity/", views.logNewActivity, name="Log New Activity"),
    path("activity/<int:id>/", views.timeLog, name="View Activity"),
    path("activity/<int:id>/deleteActivity/", views.deleteActivity, name="Delete Activity"),
    path("activity/<int:id>/newTimeLog/", views.addTimeLog, name="Log New Time Log HTML"),
    path("activity/<int:id>/newTimeLog/logNewTimeLog/", views.logNewTimeLog, name="Log New Time Log")
]