from django.shortcuts import render, HttpResponse

def home(request):
    name = ['a','b','c']
    context = {
        'name': name
    }
    return render(request, 'home.html', context)