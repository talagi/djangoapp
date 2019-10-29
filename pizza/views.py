from django.shortcuts import render
from .models import Pizza
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Witaj w barze pizza!")
    return render(request, 'pizza/index.html')

def news(request):
    # return HttpResponse("<h1>Nowości w barze.</h1>")
    return render(request, 'pizza/news.html')

def pizza(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        opis = request.POST.get('opis', '')
        rozmiar = request.POST.get('rozmiar', '')
        cena = request.POST.get('cena', '')
        if len(nazwa.strip()) and len(kod.strip()):
            p = Pizza(nazwa=nazwa, opis=opis, rozmiar=rozmiar, cena=cena)
            p.save()
            messages.success(request, "Dobrze!!!")
        else:
            messages.error(request, "Błąd danych!!!")


    pizza = Pizza.objects.all()
    kontekst = {'pizza': pizza}
    return render(request, 'pizza/pizzaformularz.html', kontekst)
