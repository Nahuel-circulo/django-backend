from django.contrib import admin
from sentidos.models import Food,Usuario,Opinion,Mesa,Reserva,Personal,Pedido
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=['id','name','description','image','price','category']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=['id','name','password','email','gender']

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display=['id','username','password','role']

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display=['id','name','comment','calification','gender']


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display=['id','nro_mesa']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=['id','nro_mesa','fecha','confirmado','comensales','user_id']

@admin.register(Pedido)
class PedidosAdmin(admin.ModelAdmin):
    list_display=['*']

