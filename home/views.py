from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('<h1> Welcome to Sujnana Coaching Center </h1>')
	return render(request, "home/home.html")
