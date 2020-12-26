from django.urls import path
from . import views

app_name = 'slo3a'

urlpatterns = [
    path('slo3a/', views.home, name='home'),
]
