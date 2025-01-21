from django.contrib import admin
from .models import *

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('user', 'poste', 'solde_conge', 'date_embauche')
    search_fields = ('user__username', 'poste')

@admin.register(TypeConge)
class TypeCongeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'jours_alloues_annuels')

@admin.register(DemandeConge)
class DemandeCongeAdmin(admin.ModelAdmin):
    list_display = ('employe', 'type_conge', 'date_debut', 'date_fin', 'statut')
    list_filter = ('statut', 'type_conge')
    search_fields = ('employe__user__username',)

    actions = ['valider_conge','rejeter_conge']

    def valider_conge(self, request, queryset):
        updated_count = queryset.update(statut='APPROUVE')
        self.message_user(request, f'{updated_count} demandes de congé validées.')
    
    valider_conge.short_description = "Valider les demandes de congé sélectionnées"


    def rejeter_conge(self, request, queryset):
        updated_count = queryset.update(statut='REJETE')
        self.message_user(request, f'{updated_count} demandes de congé validées.')
    
    rejeter_conge.short_description = "Rejeter les demandes de congé sélectionnées"
