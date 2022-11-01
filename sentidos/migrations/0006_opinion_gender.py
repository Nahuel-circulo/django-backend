# Generated by Django 4.1 on 2022-09-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sentidos", "0005_mesa_reserva"),
    ]

    operations = [
        migrations.AddField(
            model_name="opinion",
            name="gender",
            field=models.CharField(
                choices=[("H", "Hombre"), ("M", "Mujer")], default=1, max_length=7
            ),
            preserve_default=False,
        ),
    ]
