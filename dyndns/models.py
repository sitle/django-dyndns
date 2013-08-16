from django.db import models

class Parametre(models.Model):
    parametre = models.CharField(max_length=200)
    valeur = models.CharField(max_length=200)
