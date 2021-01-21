from django.shortcuts import render
from current_lesson.views import current_lesson
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/rejestracja/')
def timetable(request):
    context = {'curr_lesson': current_lesson(request, 'slo3a')[0],
               'plan': current_lesson(request, 'slo3a')[1]}

    return render(request, 'timetable/timetable.html', context=context)
