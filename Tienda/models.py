from django.db import models


# Create your models here.


class project(models.Model):
    tittle = models.CharField(max_length=200)
    descripcion = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
