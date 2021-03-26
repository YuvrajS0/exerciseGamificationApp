from django.urls import path

from . import views

app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
]
