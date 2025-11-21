from django.shortcuts import render

# Create your views here.

def page_not_found(request, exception) : 
  return render(request, 'not_found.html', status=404)

def server_error(request):
  return render(request, 'error.html', status=500)