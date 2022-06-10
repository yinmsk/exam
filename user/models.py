from django.db import models

# Create your models here.

# email, password 받는 곳
class UserModel(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

