from django.urls import path
from django.conf.urls import include

from . import views
from .views import video

app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='home'),
    path('video/', views.video, name='video'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('workout/', views.addWorkout, name='workout'),
    path('leaderboard/', views.leaderboardView, name='leaderboard'),
    path('accounts/', include('allauth.urls')),
]