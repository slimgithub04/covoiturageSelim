from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'departure_date']
        widgets = {
            'departure_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # Pour obtenir un champ datetime-local dans le formulaire
            }),
        }
