<<<<<<< HEAD
from django.urls import path
from . import views
urlpatterns = [

]
=======
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]
>>>>>>> 2107349304d3726ad311440039b24188491d769b
