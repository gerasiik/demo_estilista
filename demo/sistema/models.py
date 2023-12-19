from django.db import models
from django.utils import timezone

# Create your models here.


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    img = models.FileField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sistema"
