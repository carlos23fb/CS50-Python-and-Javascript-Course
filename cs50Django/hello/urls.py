from django.urls import path
from . import views
urlpatterns = [
    # path("<str:name>", views.greet, name="greet"),
    path('', views.index, name='index'),
    path('helloBrian', views.brian, name='brian'),
    # path('<str:name>', views.greetHtml, name="greetHtml"),
    path('<str:word>', views.evenWord, name="evenWord")
]
