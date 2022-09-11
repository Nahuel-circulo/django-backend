from django.db import models

# Create your models here.

CATEGORY_CHOICES = (('T','Tea'),('F','Food'))
GENDERS_CHOICES = (('H','Hombre'),('M','Mujer'))
HORARIO_CHOICES = (('M','Matutino'),('N','Nocturno'))

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=7)
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    category = models.CharField( max_length=7,choices=CATEGORY_CHOICES)

    
class Opinion(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    calification = models.IntegerField()


class Usuario(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    gender = models.CharField( max_length=7,choices=GENDERS_CHOICES)


class Mesa(models.Model):
    nro_mesa = models.IntegerField()


class Reserva(models.Model):
    nro_mesa = models.IntegerField()
    horario = models.CharField(max_length=10,choices=HORARIO_CHOICES)
    fecha = models.CharField(max_length=50)
    confirmado = models.BooleanField()
    comensales = models.IntegerField()

   
    
    

