from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE = [
    ('MANAGER', 'MANAGER'),
    ('COMMERCIAL', 'COMMERCIAL'),
    ('SUPPORT', 'SUPPORT'),
]


# Utilisation d'un model de base de Django Auth avec "AbstractUser"
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, default="null")
    role = models.CharField(choices=ROLE, max_length=20, default="MANAGER")

    def save(self, *args, **kwargs):
        user = super(CustomUser, self)
        if len(user.password) != 88:
            user.set_password(self.password)
        user.save()
        return user
