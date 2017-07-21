from django.http import HttpResponse
from django.shortcuts import render_to_response

# Form
def search_form(request):
    return render_to_response('search_form.html')

# Get data
def search(request):
    request.encoding="utf-8"
    if 'data' in request.GET:
        message = 'Your search message is: ' + request.GET['data']
    else:
        message = 'You have submit blank form'
    return HttpResponse(message)

