from django.shortcuts import render

# Create your views here.


def charqueadas(resquest):
    return render(resquest, 'cities/charqueadas.html')

def valeVerde(request):
    return render(request, 'cities/vale-verde.html')
