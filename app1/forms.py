from django import forms

from .models import Samochod,Marka

class CarForm(forms.ModelForm):
    class Meta:
        model = Samochod
        fields = ('marka', 'model','rok','moc','pojemnosc','przebieg','paliwo','nadwozie','kolor','cena')
        labels = {
			"moc": "Moc[KM]","pojemnosc":"Pojemnosc[cm3]","przebieg":"Przebieg[km]","cena":"Cena[zł]","paliwo":"Rodzaj paliwa","nadwozie":"Typ nadwozia"
		}

class FilterForm(forms.Form):
	iquery = Samochod.objects.order_by().values_list('marka', flat=True).distinct()
	#iquery_choices = [('', '----')] + [(id, id ) for id in iquery]
	iquery_choices = [('', '----')] 
	for id in iquery:
		obj = Marka.objects.get(pk=id)
		iquery_choices +=[(id, obj.nazwa )]
	marka = forms.ChoiceField(iquery_choices,required=False, widget=forms.Select())
	#marka = forms.ModelChoiceField (required=False,queryset = Samochod.objects.order_by().values_list('marka__nazwa',flat=True).distinct() )
	model = forms.CharField( max_length=30,required=False)
	cena_od = forms.IntegerField(min_value = 0 ,required=False)
	cena_do = forms.IntegerField(required=False)
	rok_od = forms.IntegerField(min_value = 1900,required=False)
	rok_do = forms.IntegerField(required=False)
	def clean(self):
		marka = self.cleaned_data.get('marka')
		model = self.cleaned_data.get('model')
		rok_od  = self.cleaned_data.get('rok_od')
        #if not subject and not subject1:
            #raise forms.ValidationError('Subject field is required.')
		return self.cleaned_data
