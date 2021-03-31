from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/rejestracja/')
def timers(request):
    context = {'abc': 'abc'}

    return render(request, 'timers/timers.html', context=context)
