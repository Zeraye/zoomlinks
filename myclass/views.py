from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lessons.views import lessons

# Create your views here.
@login_required(login_url='/rejestracja/')
def myclass(request):
    lessons_all = lessons(request, request.user.class_name)
    today_day_name = lessons_all[3]

    try: lessons_today = list((lessons_all[1][today_day_name]))
    except:
        lessons_today = []
        for lesson_name in lessons_all[2]:
            lessons_today.append((lesson_name, '11:30-12:30'))

    print(lessons_today)

    lessons_today = list(map(lambda lesson, time: (lesson, time), lessons_today,
        ['8:00-8:45', '8:50-9:35', '9:45-10:30', '10:40-11:25', '11:30-12:15', '12:45-13:30', '13:35-14:20', '14:25-15:10', ]))

    if today_day_name == 'Sobota' or today_day_name == 'Niedziela':
        lessons_all[0] = ''
        lessons_today = []
        for element in lessons_all[1]:
            lessons_today += lessons_all[1][element]
        lessons_today = list(set(lessons_today))

    context = {'current_lesson': lessons_all[0],
               'lessons_today': lessons_today,
               'links': lessons_all[2],
               'today_day_name': today_day_name}

    return render(request, 'myclass/myclass.html', context=context)
