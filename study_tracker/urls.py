from django.urls import path
from study_tracker.views import show_tracker, show_json, show_xml
from study_tracker.views import create_assignment

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create/', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
