from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vijay(request):
    return HttpResponse("hi i am thalapathy vijay acting as a hero")
def vijay1(request):
    return render(request,"vijay1.html")

def samantha1(request):
    return render(request,"samantha1.html")

def samantha(request):
    return HttpResponse("hi i am heroine samantha")
