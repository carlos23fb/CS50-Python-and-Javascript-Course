<<<<<<< HEAD
from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="Arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
=======
from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passanger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(
        Flight, blank=True, elated_name="passangers")

    def __str__(self):
        return f"{self.first} {self.last}"
>>>>>>> 2107349304d3726ad311440039b24188491d769b
