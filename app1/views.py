from django.shortcuts import render
from django.http import HttpResponse
from .models import Samochod

def index(request):
	return HttpResponse("Hello World. Index")

def test(request):
	lista = Samochod.objects.all()
	return render(request, 'app1/test.html', {'lista':lista})

def test2(request):
    return render(request, 'app1/test.html', {})

# Create your views here.
