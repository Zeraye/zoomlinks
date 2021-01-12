from django.shortcuts import render
from datetime import datetime

# Create your views here.
def current_lesson(plan):
    day = datetime.today().weekday()
    if day <= 4:
        lessons = plan[day]
    else:
        return 'Wolne'

    time = datetime.now().hour*60 + datetime.now().minute

    if 360 <= time <= 525: lesson_num = 0
    elif 525 < time <= 575: lesson_num = 1
    elif 575 < time <= 630: lesson_num = 2
    elif 630 < time <= 685: lesson_num = 3
    elif 685 <= time < 735: lesson_num = 4
    elif 735 < time <= 810: lesson_num = 5
    elif 810 < time <= 860: lesson_num = 6
    elif 860 < time <= 910: lesson_num = 7
    else: lesson_num = None

    if lesson_num != None and lesson_num < len(lessons):
        return lessons[lesson_num]

    else:
        return 'Wolne'
