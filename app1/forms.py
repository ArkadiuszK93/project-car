from django import forms
from .models import Samochod,Marka,Uzytkownik
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Samochod
        fields = ('marka', 'model','rok','moc','pojemnosc','przebieg','paliwo','nadwozie','kolor','cena')
        labels = {
			"moc": "Moc[KM]","pojemnosc":"Pojemnosc[cm3]","przebieg":"Przebieg[km]","cena":"Cena[zl]","paliwo":"Rodzaj paliwa","nadwozie":"Typ nadwozia"
		}

class UserForm(forms.ModelForm):
    class Meta:
        model = Uzytkownik
        exclude = ['user']

class UserCreateForm(forms.Form):
    login = forms.CharField( max_length=18,required=True)
    haslo = forms.CharField(max_length=20,min_length=4 ,required=True,widget=forms.PasswordInput())
    haslo_powtorz = forms.CharField(label="Powtórz hasło",max_length=20,min_length=4 ,required=True,widget=forms.PasswordInput())
    imie = forms.CharField( max_length=20,required=False)
    nazwisko = forms.CharField( max_length=25,required=False)
    telefon = forms.IntegerField(required=True)
    def clean(self):
        haslo = self.cleaned_data.get('haslo')
        haslo_powtorz = self.cleaned_data.get('haslo_powtorz')
        login = self.cleaned_data.get('login')

        try:
            user = User.objects.get(username=login)
        except Exception as e:
            user = None

        if user != None:
             raise forms.ValidationError("Podana nazwa użytkownika jest już zajęta")


        if haslo != haslo_powtorz:
            raise forms.ValidationError("Hasła muszą się zgadzać")

        return self.cleaned_data




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

class MarkaForm(forms.ModelForm):
    class Meta:
        model = Marka
        fields = ('nazwa','kraj_pochodzenia')
        labeles = {
            'kraj_pochodzenia': 'Kraj pochodzenia'
            }
