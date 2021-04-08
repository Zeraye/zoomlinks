from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import SettingsForm
from lessons.views import lessons

# Create your views here.
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
        return HttpResponseRedirect(reverse('myclass:myclass'))
    else:
        form = SettingsForm()
    import os
    MESSENGER_LINK = os.environ.get('MESSENGER_LINK')
    return render(request, 'settings/settings.html', {'form': form, 'current_lesson': lessons(request, request.user.class_name)[0], 'messenger_link': MESSENGER_LINK})
