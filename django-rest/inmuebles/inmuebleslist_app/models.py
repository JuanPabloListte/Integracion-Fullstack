from django.db import models
from django.core.validators import MinValueValidator as min, MaxValueValidator as max
from user_app.models import Account

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    avg_calificacion = models.FloatField(default=0)
    numero_calificacion = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="inmuebleList")
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return self.direccion + ', ' + self.pais
    
    
class Comentario(models.Model):
    comentario_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(validators=[min(1), max(5)])
    texto = models.CharField(max_length=250, null=True)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='comentarios')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.calificacion) + ' - ' + self.inmueble.direccion
    
