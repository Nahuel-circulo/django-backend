# Generated by Django 4.1 on 2022-09-13 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sentidos", "0006_opinion_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="email",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]