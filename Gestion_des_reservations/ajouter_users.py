import os
import django

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gestion_des_reservations.settings")
django.setup()

from users.models import Users

# Ajouter des utilisateurs
user1 = Users(firstname='Alice', lastname='Smith')
user1.save()

user2 = Users(firstname='Bob', lastname='Johnson')
user2.save()

user3 = Users(firstname='Charlie', lastname='Brown')
user3.save()

print("Utilisateurs ajoutés avec succès.")
