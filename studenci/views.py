from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Studenci!")
    # return render(request, 'studenci/index.html')