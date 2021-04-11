from django.urls import path

from . import views

app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.workouts, name='dashboard'),
    path('workout/', views.workout, name='workout'),
    path('leaderboard/', views.leaderboardView, name='leaderboard'),
]