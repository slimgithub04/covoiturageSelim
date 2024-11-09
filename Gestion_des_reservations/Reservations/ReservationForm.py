from django import forms
from .models import Reservation
from Trip.models import Trip  # Assurez-vous d'importer le modèle Trip

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user_id', 'Baggage', 'seat_count', 'Payment_Method']
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'seat_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'Baggage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Payment_Method': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Si l'instance existe, c'est une mise à jour
            self.fields['user_id'].widget.attrs['readonly'] = True  # Rendre le champ user_id en lecture seule

