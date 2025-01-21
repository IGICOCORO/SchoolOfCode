from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_demandes, name='liste_demandes'),
    path('demandes/creer/', views.creer_demande, name='creer_demande'),
]
