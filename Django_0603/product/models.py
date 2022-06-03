from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=256)


class Drink(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    allergy = models.CharField(max_length=256)
    nutrition = models.CharField(max_length=256)