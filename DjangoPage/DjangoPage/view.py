from django.shortcuts import render

def index(request):
    context = {}
    context['index'] = "Welcome to My First Django Page!"
    return render(request, 'index.html', context)

def exchange(request):
    context = {}
    context['exchange'] = "This is exchange page"
    return render(request, 'exchange.html', context)

