from django.shortcuts import render
from django.http import HttpResponse
from .models import Samochod

def index(request):
	return HttpResponse("Hello World. Index")

def test(request):
    lista = Samochod.objects.all()
    return render(request, 'app1/test.html', {'lista':lista})

def car_detail(request,pk):
    Samochod.objects.get(pk=pk)
    return render(request, 'app1/car_detail.html', {})

# Create your views here.
