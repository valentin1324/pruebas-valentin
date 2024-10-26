from django.db import models

# Create your models here.

class Libro(models.Model):
    libro_id = models.AutoField(primary_key=True)
    libro_nombre = models.CharField(max_length=100, verbose_name='Nombre Libro')
    libro_imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True, blank=True)
    libro_descripcion = models.TextField(verbose_name='Descripcion',null=True, blank=True)
    libro_fecha_publicacion = models.DateField(verbose_name='Fecha Publicacion',null=True, blank=True)


#python manage.py makemigratios
#nos permite crear un archivo para migrar, debemos ejecutar este comando cada vez que modifiquemos el modelo de la bd

#python manage.py migrate
#aplica las migraciones creadas, sincroniza su estructura, modificaciones etc...
    def __str__(self):
        fila = "Libro: " + self.libro_nombre + " || "  + "Descripción: " + self.libro_descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.libro_imagen.storage.delete(self.libro_imagen.name)
        super().delete()
        
    
    
    