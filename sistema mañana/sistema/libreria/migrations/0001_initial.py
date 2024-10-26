# Generated by Django 3.2.8 on 2024-10-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('libro_id', models.AutoField(primary_key=True, serialize=False)),
                ('libro_nombre', models.CharField(max_length=100, verbose_name='Nombre Libro')),
                ('libro_imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagennn')),
                ('libro_descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('libro_fecha_publicacion', models.DateField(blank=True, null=True, verbose_name='Fecha Publicacion')),
            ],
        ),
    ]
