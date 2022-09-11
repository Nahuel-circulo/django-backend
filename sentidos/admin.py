from django.contrib import admin
from sentidos.models import Food,Usuario,Opinion,Mesa,Reserva
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=['id','name','description','image','price','category']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=['id','name','password','email','gender']

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display=['id','name','comment','calification']


@admin.register(Mesa)
class OpinionAdmin(admin.ModelAdmin):
    list_display=['id','nro_mesa']

@admin.register(Reserva)
class OpinionAdmin(admin.ModelAdmin):
    list_display=['id','nro_mesa','fecha','confirmado','comensales']