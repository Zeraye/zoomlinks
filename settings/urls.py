from django.urls import path, include
from . import views

app_name = 'settings'

urlpatterns = [
    path('ustawienia/', views.settings, name='settings'),
]
