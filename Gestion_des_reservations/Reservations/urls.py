from django.urls import path
from .views import list_trips,home,select_trip,create_reservation,check_user,delete_reservation,update_reservation

urlpatterns = [
    path('', home, name='home'),  # Route pour la page d'accueil
    path('select_trip/', select_trip, name='select_trip'),  # URL pour traiter la sélection
    path('reservation/', list_trips, name='list_trips'),  # Route pour réserver un trajet
    path('create_reservation/<int:trip_id>/', create_reservation, name='create_reservation'),  # Créer une réservation
    path('check_user/', check_user, name='check_user'), 
    path('delete_reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'), 
    path('update_reservation/<int:reservation_id>/', update_reservation, name='update_reservation'), 

    
]
