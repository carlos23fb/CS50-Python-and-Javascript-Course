from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def brian(request):
    return HttpResponse("Hola, Brian!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()} !")


def greetHtml(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })


def evenWord(request, word):
    return render(request, "hello/evenWord.html", {
        "result": isEven(word),
        "word": word
    })


def isEven(word):
    """
    docstring
    """
    if len(word) % 2 == 0:
        return "Par"
    else:
        return "impar"
