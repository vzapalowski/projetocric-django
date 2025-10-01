from django.views.generic.list import ListView
from django.shortcuts import render

def devsView(request):
    return render(request, 'devs/index.html')
