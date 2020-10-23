from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50, null=True)
    

""" class IPSession(models.Model):
    client = models.ForeignKey(InternetService, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    description = models.CharField("Browser and device description", max_length=50, default='unknown')
    last_used = models.DateTimeField("Last authenticated date-time")
    created = models.DateTimeField("Creation date-time")
    blocked = models.BooleanField(default=False)
    manual = models.BooleanField("User Manualy Created", default=False)
    permanent = models.BooleanField("Is permanent", default=False) 

    def client_login(self):
        return self.client.login

    def __str__(self):  # Python 3: def __str__(self):
        return self.client.login + " " + self.ip """