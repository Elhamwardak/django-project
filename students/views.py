from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("welcome home")


def welcome(request):
    name = "karim"
    return render(request, "index.html", {"name": name})
