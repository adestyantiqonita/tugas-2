from django.shortcuts import render
from study_tracker.models import Assignment
from study_tracker.forms import AssignmentForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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