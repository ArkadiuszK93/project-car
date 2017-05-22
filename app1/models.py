from django.db import models

class Marka(models.Model):
	nazwa = models.CharField(max_length=30)
	kraj_pochodzenia = models.CharField(max_length=30)
	
class Samochod(models.Model):
	marka = models.ForeignKey(Marka)
	model = models.CharField(max_length=30)
	moc = models.IntegerField()
	pojemnosc = models.IntegerField()
	przebieg = models.IntegerField()
	paliwo = models.CharField(max_length=20)
	nadwozie = models.CharField(max_length=20)
	kolor = models.CharField(max_length=20)
	cena =  models.IntegerField()
