from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from sentidos.models import Food,Opinion,Usuario,Mesa,Reserva,Personal,Pedido,Linea_pedido


class FoodSerializer(ModelSerializer):
    class Meta:
        model=Food
        fields = ['id','name','description','price','image','category']


class OpinionSerializer(ModelSerializer):
    class Meta:
        model=Opinion
        fields = ['id','name','comment','calification','gender']


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model=Usuario
        fields = ['id','name','email','gender','password']
        extra_kwargs = {
                'password': {'write_only': True}
        }

class PersonalSerializer(ModelSerializer):
    class Meta:
        model=Personal
        fields = ['id','username','password','role']
        extra_kwargs = {
                'password': {'write_only': True}
        }


class MesaSerializer(ModelSerializer):
    class Meta:
        model=Mesa
        fields = ['id','nro_mesa']

class ReservaSerializer(ModelSerializer):
    class Meta:
        model=Reserva
        fields = ['id','nro_mesa','horario','fecha','confirmado','comensales','user_id','cancelado']


class PedidoSerializer(ModelSerializer):
    class Meta:
        model=Pedido
