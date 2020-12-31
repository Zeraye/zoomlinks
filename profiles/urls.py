from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profil/', views.home, name='home'),
    path('profil/settings', views.settings, name='settings'),
    path('klasa', views.myclass, name='myclass'),
]
