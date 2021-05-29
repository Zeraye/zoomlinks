from django.urls import path, include
from . import views

app_name = 'leagueoflegends'

urlpatterns = [
    path('lol/', views.leagueoflegends, name='leagueoflegends'),
]
