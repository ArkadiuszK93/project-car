from django.db import models
from django.contrib.auth.models import User

class Marka(models.Model):
	nazwa = models.CharField(max_length=30)
	kraj_pochodzenia = models.CharField(max_length=30)
	def __str__(self):
	    return self.nazwa


class Uzytkownik(models.Model):
    Imie = models.CharField(max_length=20,default=None)
    Nazwisko = models.CharField(max_length=30,default=None)
    telefon = models.IntegerField()
    user = models.ForeignKey(User)
    def __str__(self):
        return self.user.username

class Samochod(models.Model):
	paliwo_choices = (
	('Benzyna', 'Benzyna'),
	('Diesel', 'Diesel'),
	('LPG', 'LPG'),
	)
	nadwozie_choices = (
	('Kombi', 'Kombi'),
	('Sedan', 'Sedan'),
	('Hatchback', 'Hatchback'),
	('Kabriolet', 'Kabriolet'),
	('SUV', 'SUV'),
	('Coupe', 'Coupe'),
	)
	marka = models.ForeignKey(Marka)
	model = models.CharField(max_length=30)
	rok = models.IntegerField()
	moc = models.IntegerField()
	pojemnosc = models.IntegerField()
	przebieg = models.IntegerField()
	paliwo = models.CharField(max_length=20,choices=paliwo_choices)
	nadwozie = models.CharField(max_length=20,choices=nadwozie_choices)
	kolor = models.CharField(max_length=20)
	cena =  models.IntegerField()
	uzytkownik = models.ForeignKey(Uzytkownik)
	def __str__(self):
	    return self.marka.nazwa + ' ' + self.model

