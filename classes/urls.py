from django.urls import path, include
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.home, name='home'),
]
