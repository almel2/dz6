from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return f'name:{self.name}, Email:{self.email}, Password:{self.password}'
