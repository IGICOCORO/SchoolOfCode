from rest_framework import serializers
from .models import *

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = f"{instance.user.first_name} {instance.user.last_name}"
        return response


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ('user','solde_conge', 'date_embauche')

class TypeCongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeConge
        fields = '__all__'

class DemandeCongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeConge
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employe'] = EmployeeDetailsSerializer(instance.employe).data
        return representation