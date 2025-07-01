from django.db import models


# Create your models here.
class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    cedula=models.CharField(max_length=15)
    edad=models.CharField(max_length=10)
    tipo_sangre=models.CharField(max_length=10)
    seguro=models.CharField(max_length=10)
    direccion=models.TextField()
    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6}"
        return fila.format(self.id, self.nombre, self.cedula, self.edad, self.tipo_sangre, self.seguro, self.direccion)