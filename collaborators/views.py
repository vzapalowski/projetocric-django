from django.shortcuts import render
from .models import Collaborators

# Create your views here.

def collaborators_list(request):
    current_collaborators = Collaborators.objects.filter(is_current=True)
    former_collaborators = Collaborators.objects.filter(is_current=False)
    return render(request, 'collaborators/collaborators.html', {
        'current_collaborators': current_collaborators,
        'former_collaborators': former_collaborators
    })