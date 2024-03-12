from django.shortcuts import render, redirect
from .models import Meeting, Room
from django.forms import modelform_factory


# Create your views here.
def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
                  {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


MeetingForm = modelform_factory(Meeting, exclude=[])
