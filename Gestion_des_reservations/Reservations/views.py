from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation  # Ajoutez l'importation pour le modèle Reservation

from Trip.models import Trip  # Assurez-vous que ce modèle est défini
from .ReservationForm import ReservationForm
from users.models import Users

def list_trips(request):
    trips = Trip.objects.all()  # Récupérer tous les trajets
    for trip in trips:
        print(trip.id, trip.destination, trip.departure_date)
    

    return render(request, 'Reservations/list_trips.html', {'trips': trips})



def home(request):
    return render(request, 'home.html')  # Assurez-vous que le template 'home.html' existe

def select_trip(request):
    if request.method == 'POST':
        selected_trip_id = request.POST.get('selected_trip')  # Récupérer l'ID du trajet sélectionné
        return redirect('create_reservation', trip_id=selected_trip_id)  # Redirigez vers la vue de création de réservation
    return redirect('home')  # Redirigez vers la page d'accueil si la méthode n'est pas POST

def create_reservation(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)  # Récupérez le trajet correspondant
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)  # Ne pas encore sauvegarder
            reservation.trip_id = trip  # Associez le trajet à la réservation
            reservation.save()  # Sauvegardez la réservation
            return redirect('home')  # Redirigez vers la page d'accueil ou une autre page
    else:
        form = ReservationForm(initial={'trip_id': trip})  # Pré-remplissez le formulaire avec le trajet

    return render(request, 'Reservations/create_reservation.html', {'form': form, 'trip': trip})


def check_user(request):
    user_exists = None
    reservations = []
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = Users.objects.get(id=user_id)
            user_exists = True
            reservations = Reservation.objects.filter(user_id=user.id)
        except Users.DoesNotExist:
            user_exists = False
    return render(request, 'Reservations/check_user.html', {'user_exists': user_exists, 'reservations': reservations})


def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)  # Récupérez la réservation par son ID

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)  # Pré-remplir le formulaire avec l'instance de réservation
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('home')  # Redirigez vers une autre page après la mise à jour
    else:
        form = ReservationForm(instance=reservation)  # Pré-remplir le formulaire pour GET

    return render(request, 'Reservations/update_reservation.html', {'form': form, 'reservation': reservation})

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)  # Récupérez la réservation par son ID

    if request.method == 'POST':
        reservation.delete()  # Supprimer la réservation
        return redirect('home')  # Redirigez vers une autre page après la suppression

    return render(request, 'Reservations/delete_reservation.html', {'reservation': reservation})