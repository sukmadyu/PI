from django.db import models

# Create your models here.

class Alternatif(models.Model):
    kri=models.TextField(null=True,blank=True)
    harga=models.TextField(null=True,blank=True)
    isi=models.TextField(null=True,blank=True)
    pao=models.TextField(null=True,blank=True)
    time=models.TextField(null=True,blank=True)
    cruelty_free=models.TextField(null=True,blank=True)
