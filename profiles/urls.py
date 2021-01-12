from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    path('ustawienia/', views.settings, name='settings'),
    path('', views.myclass, name='class'),
]
