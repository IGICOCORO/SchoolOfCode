# from django.shortcuts import render, redirect, get_object_or_404
# from .models import DemandeConge, Employe
# from .forms import DemandeCongeForm

# def liste_demandes(request):
#     demandes = DemandeConge.objects.all()
    
#     for demande in demandes:
#         delta = demande.date_fin - demande.date_debut
#         demande.nombre_jours = delta.days 

#     return render(request, 'conges/liste_demandes.html', {'demandes': demandes})

# def creer_demande(request):
#     if request.method == 'POST':
#         form = DemandeCongeForm(request.POST)
#         if form.is_valid():
#             demande = form.save(commit=False)
#             demande.employe = request.user.employe
#             demande.save()
#             return redirect('liste_demandes')
#     else:
#         form = DemandeCongeForm()
#     return render(request, 'conges/creer_demande.html', {'form': form})

from rest_framework import viewsets, mixins, generics, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class EmployeViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet ):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'user__username': ['exact'],
        'user__first_name':['exact'],
        'user__last_name':['exact'],
        'poste': ['icontains'],
        'date_embauche':['gte','lte', 'exact'],
        
    }

class TypeCongeViewSet(viewsets.ModelViewSet):
    queryset = TypeConge.objects.all()
    serializer_class = TypeCongeSerializer
    permission_classes = [permissions.IsAuthenticated]

class DemandeCongeViewSet(viewsets.ModelViewSet):
    queryset = DemandeConge.objects.all()
    serializer_class = DemandeCongeSerializer
    permission_classes = [permissions.IsAuthenticated]