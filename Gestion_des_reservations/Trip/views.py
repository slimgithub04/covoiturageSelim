from django.shortcuts import render, redirect
from .form_trip import TripForm  # Assurez-vous que ce fichier existe et est correctement défini
from .models import Trip  # Assurez-vous que ce modèle est défini
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Vérifie les données nettoyées
            form.save()
            return redirect('home')  # Redirige vers la page d'accueil après l'enregistrement
    else:
        form = TripForm()  # Utilisez TripForm pour la création de trajet

    # Corrigez le chemin du template si besoin
    return render(request, 'trip/trip_test.html', {'form': form})
def list_trips(request):
    trips = Trip.objects.all()  # Récupérer tous les trajets
    return render(request, 'trip/list_trips.html', {'trips': trips})

def home(request):
    # Corrigez le chemin du template si besoin
    return render(request, 'home.html')  # Utilise le template global 'home.html'
