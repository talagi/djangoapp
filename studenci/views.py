from django.shortcuts import render
from django.http import HttpResponse
from studenci.models import Miasto, Uczelnia
from django.contrib import messages



def index(request):
    return HttpResponse("Studenci!")
    # return render(request, 'studenci/index.html')

def miasta(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        kod = request.POST.get('kod', '')
        if len(nazwa.strip()) and len(kod.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dobrze!!!")
        else:
            messages.error(request, "Błąd danych!!!")


    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        if len(nazwa.strip()):
            n = Uczelnia(nazwa=nazwa, )
            n.save()
            messages.success(request, "Dobrze!!!")
        else:
            messages.error(request, "Błąd danych!!!")

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie}
    return render(request, 'studenci/uczelnie.html', kontekst)