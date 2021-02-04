from django.shortcuts import render
from datetime import datetime

# Create your views here.
def lessons(request, class_name):
    if request.user.class_name == 'slo3a':
        timetable = {
            'Poniedziałek': ['Fizyka - Mazi', 'Informatyka', 'Angielski', 'Angielski', 'Matematyka', 'Matematyka', 'Polski'],
            'Wtorek': ['Fizyka - Mazi', 'W-f', 'Polski', 'Polski', 'Informatyka', 'Matematyka', 'Matematyka'],
            'Środa': ['Fizyka - Radek', 'Fizyka - Radek', 'Matematyka', 'Matematyka', 'His', 'Fizyka - Mazi', 'Polski'],
            'Czwartek': ['Fizyka - Radek', 'Matematyka', 'Matematyka', 'Angielski', 'Wychowawcza', 'Informatyka', 'W-f', 'Religia'],
            'Piątek': ['W-f', 'Religia', 'Polski', 'Fizyka - Mazi', 'Matematyka', 'Angielski', 'Angielski']
        }

        links = {
            'Matematyka': 'https://us04web.zoom.us/j/2483015118?pwd=WEtHK0llaWZmTWtmTnhPUlVqRmlGUT09',
            'Fizyka - Mazi': 'https://zoom.us/j/2838246804?pwd=Umh1eEJ5VFJqVE1NSmZZUytlMUdGZz09',
            'Fizyka - Radek': 'https://zoom.us/j/4861451584?pwd=RFFxWGRJelE2T3BtdWpQUk5SQjFBQT09',
            'Angielski': 'https://us04web.zoom.us/j/6708313679?pwd=RWlUODlGOTFndFZSbHBRdFZoT0V3dz09',
            'Polski': 'https://us04web.zoom.us/j/9760904503?pwd=azByY3htY3hmOURmamxob3hQL1pDQT09',
            'Religia': 'https://us04web.zoom.us/j/9625315964?pwd=SFNmQUIvT0tRaHlDaVYrN3l5bzJVQT09',
            # garbacik
            'Wychowawcza': 'https://us04web.zoom.us/j/8098106082?pwd=UjR1RVN0T2d0bXpNcnZjaTJheHpFQT09',
            # miska
            # 'Wychowawcza': 'https://us04web.zoom.us/j/2225987302?pwd=dkYyNUU0V0hoUEdZckVsVWFRZzlXQT09',
            'His': 'https://us04web.zoom.us/j/78026871274?pwd=ZUhtV0M0cGE2RXROREFkS2t1THFZUT09'
        }

        if request.user.math_teacher == 'Buba':
            links['Matematyka'] = 'https://us04web.zoom.us/j/2483015118?pwd=WEtHK0llaWZmTWtmTnhPUlVqRmlGUT09'
        elif request.user.math_teacher == 'Rubaj':
            links['Matematyka'] = 'https://us02web.zoom.us/j/2693771475?pwd=SFNmQUIvT0tRaHlDaVYrN3l5bzJVQT09'

        if request.user.english_teacher == 'Denys':
            links['Angielski'] = 'https://us04web.zoom.us/j/6708313679?pwd=RWlUODlGOTFndFZSbHBRdFZoT0V3dz09'
        elif request.user.english_teacher == 'Kotlińska':
            links['Angielski'] = 'https://us04web.zoom.us/j/75537981297?pwd=L3BHL0tkZXFsTEx5VjV3WS8yQ2VJUT09'
        elif request.user.english_teacher == 'Skowron':
            links['Angielski'] = 'https://zoom.us/j/6717774670?pwd=REhhSXdCaXphRFQyM0pVUGJ3THFBZz09'
        elif request.user.english_teacher == 'Kowalczyk':
            links['Angielski'] = 'https://us04web.zoom.us/j/4312598558?pwd=RDlUelJXTk1mUmxoMzNPOUZJa2IxZz09'

    day = datetime.today().weekday()
    time = datetime.now().hour*60 + datetime.now().minute
    lesson_name = 'Wolne'

    if day == 0: day_name = 'Poniedziałek'
    if day == 1: day_name = 'Wtorek'
    if day == 2: day_name = 'Środa'
    if day == 3: day_name = 'Czwartek'
    if day == 4: day_name = 'Piątek'
    if day == 5: day_name = 'Sobota'
    if day == 6: day_name = 'Niedziela'

    if day <= 4:
        today_lessons = timetable[day_name]
        if 360 < time <= 525: lesson_number = 0
        elif 525 < time <= 575: lesson_number = 1
        elif 575 < time <= 630: lesson_number = 2
        elif 630 < time <= 685: lesson_number = 3
        elif 685 < time <= 735: lesson_number = 4
        elif 735 < time <= 810: lesson_number = 5
        elif 810 < time <= 860: lesson_number = 6
        elif 860 < time <= 910: lesson_number = 7
        else: lesson_number = None

        if lesson_number != None and lesson_number < len(today_lessons):
            lesson_name = today_lessons[lesson_number]

    return lesson_name, timetable, links, day_name
