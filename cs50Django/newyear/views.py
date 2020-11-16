from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def index(request):
    return render(request, "newyear/index.html")


def newYear(request):
    now = datetime.datetime.now()
    return render(request, "newyear/newYear.html", {
        "newyear": now.month == 1 and now.day == 1
    })

def hello(request):
    return HttpResponse("Hi")
