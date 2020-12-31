from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('rejestracja/', views.SignUp.as_view(), name='signup'),
    path('logowanie/', views.Login.as_view(), name='login'),
    path('wylogowywanie/', views.Logout.as_view(), name='logout'),
]
