from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .chatbot_api import chatbot as cb

# Create your views here.
@login_required(login_url='/rejestracja/')
def chatbot(request):
    context = {'messages': [('bot', 'Cześć, co tam u Ciebie?')]}

    if request.method == 'POST':
        if request.POST['message-value'] != '':
            command = "context = {'messages': " + request.POST['past-messages'] + "}"
            lcls = locals()
            exec(command, globals(), lcls)
            context = lcls["context"]

            message = request.POST['message-value']
            context['messages'].append(('my', message))
            answer = cb.find_answer(message)
            context['messages'].append(('bot', answer))


    return render(request, 'chatbot/chatbot.html', context=context)
