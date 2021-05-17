from django.shortcuts import render

# Create your views here.
def temporary(request):
    context = {}
    return render(request, 'temporary/temporary.html', context=context)

