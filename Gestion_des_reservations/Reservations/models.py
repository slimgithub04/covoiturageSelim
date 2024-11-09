from django.db import models
from Trip.models import Trip
from users.models import Users

# Create your models here.
class Reservation(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    # trip_id=models.CharField(max_length=10)
    #user_id=models.CharField(max_length=10)
    reservation_date = models.DateTimeField(auto_now_add=True)
    Baggage=models.BooleanField(default=False) 
    seat_count=models.IntegerField()
    Payment_Method_list = [
        (' online_payment', ' online_payment'),
        ('cash_payment', 'cash_payment'),
       
    ]
    status_cases = [
        ('cancel', ' cancel'),
        ('on_hold', 'on_hold'),
        ('confirmed', 'confirmed')
       
    ]
    status=models.CharField(max_length=20,choices=status_cases)
    Payment_Method=models.CharField(max_length=20,choices=Payment_Method_list)

    class Meta:
        unique_together = ('user_id', 'trip_id')  # Contrainte unique
    def __str__(self):
        return f"Reservation for trip {self.trip_id} by user {self.user_id}"
