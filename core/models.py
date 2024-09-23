from django.db import models

class Usuarios(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    apellido = models.CharField(max_length=200, verbose_name="Apellido")
    mail = models.EmailField(blank=True, verbose_name="Email")
    apodo = models.CharField(max_length=200, verbose_name="Apodo")
    image = models.ImageField(verbose_name="Imagen",null=True,)
    disponibilidad = models.BooleanField(default=True, verbose_name="Disponibilidad")
    rol = models.CharField(max_length=200, verbose_name="Rol", blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")  # Opcional
    honor = models.IntegerField(null=True,blank=True, verbose_name="Honor",default=100)
    estado = models.BooleanField(null=True,default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
        ordering = ["-created"]

    def __str__(self):
        return self.nombre





























