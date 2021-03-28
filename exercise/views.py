from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views import View
from .models import Workout
from django.utils import timezone


def index(request):
    return render(request, 'exercise/index.html')

def workout(request):
    render(request, 'exercise/index.html')
    if request.method == 'POST':
        workout=Workout()
        workout.user = request.user
        workout.workout_title= request.POST.get('workout_title')
        workout.workout_pub_date= request.POST.get('workout_pub_date')
        workout.workout_start_time = request.POST.get('workout_start_time')
        workout.workout_end_time = request.POST.get('workout_end_time')
        workout.workout_description = request.POST.get('workout_description')
        workout.save()        
    return render(request, 'exercise/workout.html')  

def workouts(request):
    render(request, 'exercise/index.html')
    workout_dict = Workout.objects.filter(user=request.user)
    return render(request, 'exercise/dashboard.html', {'workout_dict': workout_dict})

