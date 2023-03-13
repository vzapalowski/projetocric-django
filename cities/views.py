from django.shortcuts import render

def charqueadas(resquest):
    return render(resquest, 'cities/charqueadas.html')

def vale_verde(request):
    return render(request, 'cities/vale_verde.html')
