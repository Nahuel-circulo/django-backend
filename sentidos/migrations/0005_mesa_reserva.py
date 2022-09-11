# Generated by Django 4.1 on 2022-09-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentidos', '0004_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_mesa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_mesa', models.IntegerField()),
                ('horario', models.CharField(choices=[('M', 'Matutino'), ('N', 'Nocturno')], max_length=10)),
                ('fecha', models.CharField(max_length=50)),
                ('confirmado', models.BooleanField()),
                ('comensales', models.IntegerField()),
            ],
        ),
    ]
