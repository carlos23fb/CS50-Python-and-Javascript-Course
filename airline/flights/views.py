<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.http import HttpResponseRedirect
from flights.models import Flight, Passanger
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):

    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passangers": flight.passangers.all(),
        "non_passangers": Passanger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passanger = Passanger.objects.get(pk=int(request.POST["passanger"]))
        passanger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
>>>>>>> 2107349304d3726ad311440039b24188491d769b
