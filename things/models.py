from django.db import models


class Thing(models.Model):

    name = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
