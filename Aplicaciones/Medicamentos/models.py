from django.db import models

# Create your models here.
class Medicamento(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    laboratorio=models.CharField(max_length=100)
    dosis=models.TextField()
    presentacion=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)
    caducidad=models.CharField(max_length=100)
    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6}"
        return fila.format(self.id, self.nombre, self.laboratorio,self.dosis,self.presentacion,self.precio,self.caducidad)