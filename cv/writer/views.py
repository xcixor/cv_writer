from django.shortcuts import render
from django.http import HttpResponse

# my views

def index(request):
    return render(request, 'writer/index.html')
