from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import create_assignment

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create/', create_assignment, name='create_assignment'),
]
