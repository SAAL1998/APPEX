from django.db import models
class info(models.Model):
    name=models.CharField(max_length=55)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)