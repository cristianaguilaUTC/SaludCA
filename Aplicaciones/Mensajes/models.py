from django.db import models

# Create your models here.
class Mensaje(models.Model):
    id=models.AutoField(primary_key=True)
    remitente=models.CharField(max_length=100)
    destinatario=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    fecha=models.CharField(max_length=100)
    asunto=models.CharField(max_length=100)
    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5}"
        return fila.format(self.id, self.remitente,self.destinatario,self.contenido,self.fecha,self.asunto)