from flights.models import Flight, Airport
from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
