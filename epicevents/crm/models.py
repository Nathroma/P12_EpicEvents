from django.db import models
from django.db.models.query_utils import refs_expression
from pkg_resources import require
from management.models import CustomUser

# Model "Client" suivant example donné
class Client(models.Model):
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    prospect = models.BooleanField(default=True)
    compagny = models.CharField(max_length=250, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    sale_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)


# Model "Contrat" suivant example donné
class Contract(models.Model):
    sales_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contract')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    amount = models.IntegerField()
    payment_due = models.DateTimeField()


# Model "Evenement" suivant example donné
class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='event')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    event_status = models.BooleanField(default=True)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=2048)
