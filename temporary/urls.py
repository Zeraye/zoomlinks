from django.urls import path, include
from . import views

app_name = 'temporary'

urlpatterns = [
    path('', views.temporary, name='temporary'),
]
