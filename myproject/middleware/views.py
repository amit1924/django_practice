from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    print("I am view")
    return HttpResponse("this is my home page")
