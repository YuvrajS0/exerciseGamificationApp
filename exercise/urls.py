from django.urls import path

from . import views

app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('workout/', views.addWorkout, name='workout'),
    path('leaderboard/', views.leaderboardView, name='leaderboard'),
]