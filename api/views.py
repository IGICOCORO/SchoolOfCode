from django.shortcuts import render, redirect, get_object_or_404
from .models import DemandeConge, Employe
from .forms import DemandeCongeForm

def liste_demandes(request):
    demandes = DemandeConge.objects.all()
    
    for demande in demandes:
        delta = demande.date_fin - demande.date_debut
        demande.nombre_jours = delta.days 

    return render(request, 'conges/liste_demandes.html', {'demandes': demandes})

def creer_demande(request):
    if request.method == 'POST':
        form = DemandeCongeForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.employe = request.user.employe
            demande.save()
            return redirect('liste_demandes')
    else:
        form = DemandeCongeForm()
    return render(request, 'conges/creer_demande.html', {'form': form})
