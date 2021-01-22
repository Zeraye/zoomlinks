from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lessons.views import lessons

# Create your views here.
@login_required(login_url='/rejestracja/')
def myclass(request):
    lessons_all = lessons(request, request.user.class_name)
    today_day_name = lessons_all[3]

    try: lessons_today = list(set(lessons_all[1][today_day_name]))
    except:
        lessons_today = []
        for lesson_name in lessons_all[2]:
            lessons_today.append(lesson_name)

    context = {'current_lesson': lessons_all[0],
               'lessons_today': lessons_today,
               'links': lessons_all[2],
               'today_day_name': today_day_name}

    return render(request, 'myclass/myclass.html', context=context)
