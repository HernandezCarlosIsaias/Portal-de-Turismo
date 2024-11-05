# Generated by Django 5.1.1 on 2024-10-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0007_rename_contacto_city_descripcion_remove_city_visitar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lugar_turistico',
            old_name='visitar',
            new_name='visitar1',
        ),
        migrations.RemoveField(
            model_name='city',
            name='poblacion',
        ),
        migrations.AddField(
            model_name='lugar_turistico',
            name='visitar2',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='lugar_turistico',
            name='visitar3',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]