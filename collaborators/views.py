from django.shortcuts import render
from .models import Collaborators

# Create your views here.

def collaborators_list(request):
    collabs = Collaborators.objects.all()
    return render(request, 'collaborators/index.html', {'colaboradores': collabs})