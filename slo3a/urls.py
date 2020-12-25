from django.urls import path
from . import views

app_name = 'slo3a'

urlpatterns = [
    path('slo3a/', views.home, name='home'),
    path('slo3a/matematyka', views.math, name='math'),
    path('slo3a/fizyka', views.physics, name='physics'),
    path('slo3a/angielski', views.english, name='english'),
]
