from django.shortcuts import render
from study_tracker.models import Assignment
from study_tracker.forms import AssignmentForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers

# Create your views here.
def show_tracker(request):
    assignment_data = Assignment.objects.all().values()
    response = {'assignment_data': assignment_data}
    return render(request, "tracker.html", response)

def create_assignment(request):
    form = AssignmentForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:show_tracker'))
    else:
        form = AssignmentForm()

    context = {'form': form}
    return render(request, "create_assignment.html", context)

def show_xml(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
