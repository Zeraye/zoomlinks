from django.shortcuts import render
from lessons.views import lessons
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/rejestracja/')
def timetable(request):
    lessons_all = lessons(request, request.user.class_name)
    import os
    MESSENGER_LINK = os.environ.get('MESSENGER_LINK')
    context = {'current_lesson': lessons_all[0],
               'timetable': lessons_all[1],
               'links': lessons_all[2],
               'today_day_name': lessons_all[3],
               'messenger_link': MESSENGER_LINK}

    return render(request, 'timetable/timetable.html', context=context)
