from django.db import models

# Create your models here.

CATEGORY_CHOICES = (('T','Tea'),('F','Food'))
GENDERS_CHOICES = (('H','Hombre'),('M','Mujer'))
HORARIO_CHOICES = (('M','Matutino'),('N','Nocturno'))
ROLES_CHOICES = (('Ma','Maitre'),('P','Propietario'),('Mz','Mozo'),('C','Cajero'))

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
    gender = models.CharField( max_length=7,choices=GENDERS_CHOICES)


class Usuario(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    gender = models.CharField( max_length=7,choices=GENDERS_CHOICES)


class Mesa(models.Model):
    nro_mesa = models.IntegerField()


class Reserva(models.Model):
    nro_mesa = models.IntegerField()
    horario = models.CharField(max_length=10,choices=HORARIO_CHOICES)
    fecha = models.CharField(max_length=50)
    confirmado = models.BooleanField()
    cancelado = models.BooleanField()
    comensales = models.IntegerField()
    user_id = models.IntegerField()

class Personal(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    role = models.CharField( max_length=7,choices=ROLES_CHOICES)

class Pedido (models.Model):
    user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class Linea_pedido(models.Model):
    factura = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    product = models.ForeignKey(Food,on_delete=models.CASCADE)






