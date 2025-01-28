from django.db import models
from django.contrib.auth.models import User


class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    poste = models.CharField(max_length=100, blank=True, null=True)
    date_embauche = models.DateField()
    solde_conge = models.FloatField(default=30)

    def __str__(self):
        return self.user.username

class TypeConge(models.Model):
    nom = models.CharField(max_length=50)
    jours_alloues_annuels = models.IntegerField()

    def __str__(self):
        return self.nom

class DemandeConge(models.Model):
    STATUTS = [
        ('EN_ATTENTE', 'En attente'),
        ('APPROUVE', 'Approuvé'),
        ('REJETE', 'Rejeté'),
    ]

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    type_conge = models.ForeignKey(TypeConge, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUTS,default='EN_ATTENTE')
    raison = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employe.user.username} - {self.type_conge.nom}"


# RESTFUL API 
#  Protocol HTTP, HTTPS 
#  Method GET, POST, PUT, DELETE, PATCH, OPTIONS
#  URL( endpoints) ex: http://127.0.0.1:8000/getDemandes/
