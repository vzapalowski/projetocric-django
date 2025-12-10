from django.shortcuts import render
from .models import Collaborators

# Create your views here.

def collaborators_list(request):
    collaborators = Collaborators.objects.all()
    return render(request, 'collaborators/collaborators.html', {'collaborators': collaborators})