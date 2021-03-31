from django.urls import path, include
from . import views

app_name = 'timers'

urlpatterns = [
    path('polski/', views.timers, name='timers'),
]
