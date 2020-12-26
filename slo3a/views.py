from django.shortcuts import render
from current_lesson.views import current_lesson

# Create your views here.
def home(request):
    plan = [
        ['Fizyka - Mazi', 'Informatyka', 'Angielski', 'Angielski', 'Matematyka', 'Polski'],
        ['Fizyka - Mazi', 'W-f', 'Polski', 'Polski', 'Informatyka', 'Matematyka', 'Matematyka'],
        ['Fizyka - Radek', 'Fizyka - Radek', 'Matematyka', 'Matematyka', 'His', 'Fizyka - Mazi', 'Polski'],
        ['Fizyka - Radek', 'Matematyka', 'Matematyka', 'Angielski', 'Wychowawcza', 'Informatyka', 'W-f', 'Religia'],
        ['W-f', 'Religia', 'Polski', 'Fizyka - Mazi', 'Matematyka', 'Angielski', 'Angielski']
    ]

    context = {'curr_lesson': current_lesson(plan)}

    return render(request, 'slo3a/home.html', context=context)