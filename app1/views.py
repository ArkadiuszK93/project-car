from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Samochod,Uzytkownik
from .forms import CarForm
from django.shortcuts import redirect

def index(request):
	#return HttpResponse("Hello World. Index")
	return render(request,'app1/index.html', {})

def test(request):
    lista = Samochod.objects.all()
    return render(request, 'app1/test.html', {'lista':lista})

def car_details(request,pk):
    samochod = get_object_or_404(Samochod, pk=pk)
    return render(request, 'app1/car_details.html', {'sam':samochod})

def car_add(request):
    if request.method == "POST":
        form=CarForm(request.POST);
        if form.is_valid():
            car = form.save(commit=False)
            user = Uzytkownik.objects.get(pk=1)
            car.uzytkownik = user
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form=CarForm()
        return render(request,'app1/car_add.html',{'form':form})

# Create your views here.
