from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World. Index")

def test(request):
    return render(request, 'app1/test.html', {})


# Create your views here.
