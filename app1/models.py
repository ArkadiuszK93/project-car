from django.db import models

class Marka(models.Model):
	nazwa = models.CharField(max_length=30)
	kraj_pochodzenia = models.CharField(max_length=30)
	def __str__(self):
	    return self.nazwa


class Uzytkownik(models.Model):
	login = models.CharField(max_length=30, unique=True)
	haslo = models.CharField(max_length=20)
	imie = models.CharField(max_length=20)
	nazwisko = models.CharField(max_length=25)
	telefon = models.IntegerField()
	def __str__(self):
	    return self.login

class Samochod(models.Model):
	marka = models.ForeignKey(Marka)
	model = models.CharField(max_length=30)
	rok = models.IntegerField()
	moc = models.IntegerField()
	pojemnosc = models.IntegerField()
	przebieg = models.IntegerField()
	paliwo = models.CharField(max_length=20)
	nadwozie = models.CharField(max_length=20)
	kolor = models.CharField(max_length=20)
	cena =  models.IntegerField()
	uzytkownik = models.ForeignKey(Uzytkownik)
	def __str__(self):
	    return self.marka.nazwa + ' ' + self.model

