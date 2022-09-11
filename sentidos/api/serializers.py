from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from sentidos.models import Food,Opinion,Usuario,Mesa,Reserva


class FoodSerializer(ModelSerializer):
    class Meta:
        model=Food
        fields = ['id','name','description','price','image','category']


class OpinionSerializer(ModelSerializer):
    class Meta:
        model=Opinion
        fields = ['id','name','comment','calification']


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model=Usuario
        fields = ['id','name','email','gender']


class MesaSerializer(ModelSerializer):
    class Meta:
        model=Mesa
        fields = ['id','nro_mesa']

class ReservaSerializer(ModelSerializer):
    class Meta:
        model=Reserva
        fields = ['id','nro_mesa','horario','fecha','confirmado','comensales']