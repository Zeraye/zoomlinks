from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import SettingsForm
from django import forms
from django.urls import reverse
from current_lesson.views import current_lesson

@login_required(login_url='/rejestracja/')
def settings(request):
    def subject_saving(request, subject):
        try:
            exec(f"{subject} = request.POST.get('{subject}')")
            exec(f"request.user.{subject} = {subject}")
            request.user.save()
        except:
            pass
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        teachers = ['math_teacher', 'english_teacher', 'physics_teacher',
            'biology_teacher', 'chemistry_teacher', 'geography_teacher',
            'history_teacher', 'polish_teacher', 'pe_teacher', 'german_teacher',
            'spanish_teacher', 'french_teacher', 'russian_teacher']

        for teacher in teachers:
            subject_saving(request, teacher)

        if form.is_valid():
            pass  # does nothing, just trigger the validation
        return HttpResponseRedirect(reverse('profiles:class'))
    else:
        form = SettingsForm()
    return render(request, 'profiles/settings.html', {'form': form})

@login_required(login_url='/rejestracja/')
def myclass(request):
    if request.user.class_name == 'slo3a':
        plan = [
            ['Fizyka - Mazi', 'Informatyka', 'Angielski', 'Angielski', 'Matematyka', 'Polski'],
            ['Fizyka - Mazi', 'W-f', 'Polski', 'Polski', 'Informatyka', 'Matematyka', 'Matematyka'],
            ['Fizyka - Radek', 'Fizyka - Radek', 'Matematyka', 'Matematyka', 'His', 'Fizyka - Mazi', 'Polski'],
            ['Fizyka - Radek', 'Matematyka', 'Matematyka', 'Angielski', 'Wychowawcza', 'Informatyka', 'W-f', 'Religia'],
            ['W-f', 'Religia', 'Polski', 'Fizyka - Mazi', 'Matematyka', 'Angielski', 'Angielski']
        ]

    context = {'curr_lesson': current_lesson(plan)}

    return render(request, 'profiles/class.html', context=context)
