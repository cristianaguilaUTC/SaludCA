from django.db import models

# Create your models here.
class Medico(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=100)
    consultorio=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    licencia=models.CharField(max_length=100)
    contacto=models.CharField(max_length=15)
    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6}"
        return fila.format(self.id, self.nombre, self.especialidad,self.consultorio,self.horario,self.licencia,self.contacto)