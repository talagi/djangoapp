from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from studenci.models import Miasto, Uczelnia
from studenci.forms import StudentLoginForm, UczelniaForm, MiastaForm

def index(request):
    # return HttpResponse("Witaj w aplikacji Studenci!")
    return render(request, 'studenci/index.html')


def miasta(request):
    if request.method == 'POST':
        #nazwa = request.POST.get('nazwa', '')
        #kod = request.POST.get('kod', '')
        #if len(nazwa.strip()) and len(kod.strip()):
        form = MiastaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Dobrze!!!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Ło ty oszukisto skubany!!!")
    else:
        form = MiastaForm()
    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta, 'form': form}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):

    if request.method == 'POST':
        form = UczelniaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Dane zapisano!")
            # przekierowanie
            return redirect(reverse('studenci:uczelnie'))
    else:
        form = UczelniaForm()

    uczelnie = Uczelnia.objects.all()
    kontekst = {
        'form': form,
        'uczelnie': uczelnie
    }

    return render(request, 'studenci/uczelnie.html', kontekst)


def login(request):
    if request.method == 'POST':
        pass
    else:
        form = StudentLoginForm()

    kontekst = { 'form': form }
    return render(request, 'studenci/login.html', kontekst)