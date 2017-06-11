from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Samochod,Uzytkownik
from .forms import CarForm,FilterForm,UserForm
from django.shortcuts import redirect
import pdb
#pdb.set_trace()

def index(request):
	#return HttpResponse("Hello World. Index")
	return render(request,'app1/index.html', {})

def test(request):
    #lista = Samochod.objects.all()
    lista = Samochod.objects.all()
    return render(request, 'app1/test.html', {'lista':lista})

def car_details(request,pk):
    car = get_object_or_404(Samochod, pk=pk)
    return render(request, 'app1/car_details.html', {'car':car})

def car_add(request):
    if request.method == "POST":
        form=CarForm(request.POST);
        if form.is_valid():
            car = form.save(commit=False)
            user = Uzytkownik.objects.get(user__username=request.user.username)
            car.uzytkownik = user
            car.save()
            return redirect('test')
    else:
        form=CarForm()
        return render(request,'app1/car_add.html',{'form':form})

def car_edit(request, pk):
	car = get_object_or_404(Samochod, pk=pk)
	if request.method == "POST":
		form = CarForm(request.POST, instance=car)
		if form.is_valid():
			car = form.save(commit=False)
			car.save()
			return redirect('user_details')
	else:
		form = CarForm(instance=car)
		return render(request, 'app1/car_edit.html', {'form': form})

def car_remove(request, pk):
    car = get_object_or_404(Samochod, pk=pk)
    car.delete()
    return redirect('user_details')

def car_filter(request):
	if request.method == "POST":
		form = FilterForm(request.POST)
		#a = request.POST.get('model')
		if form.is_valid():
		#print form['my_field'].value()
		#rok = form['rok_od'].value()
		#rok= form.data['rok_od']
		#lista = Samochod.objects.filter(rok__gte=rok)
		#rok=form.cleaned_data['rok_od']
			#form.clean()
			marka=form.cleaned_data['marka']
			model=form.cleaned_data['model']
			rok_od=form.cleaned_data['rok_od']
			rok_do=form.cleaned_data['rok_do']
			cena_od=form.cleaned_data['cena_od']
			cena_do=form.cleaned_data['cena_do']
			if  not marka and not model and not rok_od and not rok_do and not cena_od and not cena_do:
				lista = Samochod.objects.all()
				return render(request, 'app1/test.html', {'lista':lista})
			else:
				lista = Samochod.objects.all()
				if marka:
					lista = lista.filter(marka = marka)
				if model:
					lista = lista.filter(model__iexact = model)
				if rok_od:
					lista = lista.filter(rok__gte = rok_od)
				if rok_do:
					lista = lista.filter(rok__lte = rok_do)
				if cena_od:
					lista = lista.filter(cena__gte = cena_od)
				if cena_do:
					lista = lista.filter(cena__lte = cena_do)
				return render(request, 'app1/test.html', {'lista':lista})
			#return render(request,'app1/car_filter.html', {'form': data})
		else:
			return render(request,'app1/car_filter.html', {'form': form.errors})
		#return render(request, 'app1/test.html', {'lista':lista})
		#return redirect('test')
		#if form.is_valid():
		#return redirect('filter', form=form)
		#return redirect('test')
			#return redirect('filter', form=form)
			#return render(request,'app1/car_filter.html', {'form': form.instance.marka})
	else:
		form = FilterForm()
		return render(request,'app1/car_filter.html', {'form': form})

def user_details(request):
    user = Uzytkownik.objects.get(user__username=request.user.username)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            us = form.save(commit=False)
            us.save()
            return redirect('user_details')
    else:
        lista = Samochod.objects.filter(uzytkownik__user__username = request.user.username)
        form = UserForm(instance=user)
        return render(request,'app1/user_details.html', {'u': form,'cars': lista})
    #return render(request,'app1/user_details.html', {'u': user})
