from django.shortcuts import render
from django.views.generic.list import ListView
from routes.models import Route

class PostHome(ListView):
    template_name = 'home/index.html'
    model = Route

# def index(request):
#     return render(request, 'home/index.html')