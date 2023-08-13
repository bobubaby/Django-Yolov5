from django.db import models

class user(models.Model):
    username = models.CharField(max_length=255, unique=True)    # unique=True 不能有相同值
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    time = models.DateField(auto_now_add=True)


