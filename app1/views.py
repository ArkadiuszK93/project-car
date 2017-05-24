from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Samochod

def index(request):
	return HttpResponse("Hello World. Index")

def test(request):
    lista = Samochod.objects.all()
    return render(request, 'app1/test.html', {'lista':lista})

def car_details(request,pk):
    samochod = get_object_or_404(Samochod, pk=pk)
    return render(request, 'app1/car_details.html', {'sam':samochod})

# Create your views here.
