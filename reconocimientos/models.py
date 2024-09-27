from django.db import models
from core.models import Usuarios

class Medallas(models.Model):
    medalla_id = models.AutoField(primary_key=True)
    nombre_medalla = models.CharField(max_length=60, verbose_name="Nombre")
    desc_medalla = models.CharField(max_length=250, verbose_name="Descripción")
    image_medalla = models.ImageField(verbose_name="Logo",null=True,)
    puntos_por_nivel = models.IntegerField(verbose_name="Puntos por Nivel",default=4)
    nivel_maximo = models.IntegerField(verbose_name="Nivel Máximo",default=25)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        verbose_name = 'Medalla'
        verbose_name_plural = 'Medallas'
        ordering = ["-created"]

    def __str__(self):
        return self.nombre_medalla
    
class Titulos(models.Model):

    titulo_id = models.AutoField(primary_key=True)
    nombre_titulo = models.CharField(max_length=60, verbose_name="Nombre")
    desc_titulo = models.CharField(max_length=250, verbose_name="Descripción")
    image_titulo = models.ImageField(verbose_name="Logo",null=True,)
    es_positivo = models.BooleanField(default=True, verbose_name="¿Es positivo?")
    es_exclusivo = models.BooleanField(default=True, verbose_name="¿Es exclusivo?")
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'
        ordering = ["-created"]

    def __str__(self):
        return self.nombre_titulo
    
class MedallasPorPersona(models.Model):
    
    medalla_id = models.ForeignKey(Medallas, verbose_name="Medalla",on_delete=models.CASCADE)
    user = models.ForeignKey(Usuarios,verbose_name="Usuarios",on_delete=models.CASCADE)
    puntos_experiencia = models.IntegerField(verbose_name="Puntos XP",default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        verbose_name = 'MedallaPorPersona'
        verbose_name_plural = 'MedallasPorPersona'
        ordering = ["-created"]

    def __str__(self):
        return self.user + self.medalla_id
    
    
class TitulosPorPersona(models.Model):

    titulo_id = models.ForeignKey(Titulos, verbose_name="Título",on_delete=models.CASCADE)
    user = models.ForeignKey(Usuarios,verbose_name="Usuarios",on_delete=models.CASCADE)
    fecha_registro = models.DateField(null=True, blank=True, verbose_name="Fecha de asignación")
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        verbose_name = 'TituloPorPersona'
        verbose_name_plural = 'TitulosPorPersona'
        ordering = ["-created"]

    def __str__(self):
        return self.titulo_id + self.user