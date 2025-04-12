from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) #es formato string
    contenido = models.TextField() #es formato texto
    fecha_publicacion = models.DateTimeField(auto_now_add=True) #es formato fecha y hora, se agrega automaticamente

    def __str__(self):
        return self.title
    