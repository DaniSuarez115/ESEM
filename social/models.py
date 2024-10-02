from django.db import models
from core.models import Usuarios
# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo") 
    descripcion = models.CharField(max_length=200, verbose_name="Descripción") 
    fecha = models.DateField(verbose_name="Fecha Publicación")
    imagen = models.ImageField(verbose_name="Imagen",null=True,upload_to="social")
    user = models.ForeignKey(Usuarios,verbose_name="Usuarios",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural ='Publicaciones'
        ordering = ["-created"]
    
    def __str__(self):
        return self.titulo