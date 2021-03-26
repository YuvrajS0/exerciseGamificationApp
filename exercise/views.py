from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views import View
from .models import Workout
from django.utils import timezone


def index(request):
# Render the HTML template index.html
    return render(request, 'exercise/index.html')

def dashboard(request):
# Render the HTML template index.html

    return render(request, 'exercise/dashboard.html')