# Generated by Django 4.2.4 on 2023-09-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coreBlog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="descripcion",
            field=models.TextField(
                default=1, max_length=400, verbose_name="Descripcion"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprofile",
            name="edad",
            field=models.PositiveIntegerField(default=1, verbose_name="edad"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprofile",
            name="sexo",
            field=models.CharField(
                choices=[("M", "Hombre"), ("F", "Mujer")], default=1, max_length=20
            ),
            preserve_default=False,
        ),
    ]