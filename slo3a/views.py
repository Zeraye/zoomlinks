from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'slo3a/home.html')
