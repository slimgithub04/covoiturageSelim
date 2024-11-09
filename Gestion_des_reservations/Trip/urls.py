# urls.py
from django.urls import path
from .views import create_trip, home,list_trips  # Importez la bonne vue

urlpatterns = [
    path('', home, name='home'),  # Route pour la page d'accueil
    path('listTrajet/', list_trips, name='list_trips'),  # Route pour la page d'accueil
    path('test/', create_trip, name='trip_test'),  # Route pour créer un trajet
]
