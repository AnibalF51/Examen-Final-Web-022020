from django.db import models

class Equipos(models.Model):
    pro = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    class Meta:
        db_table = "equipo"