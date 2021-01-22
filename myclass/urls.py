from django.urls import path, include
from . import views

app_name = 'myclass'

urlpatterns = [
    path('', views.myclass, name='myclass'),
]
