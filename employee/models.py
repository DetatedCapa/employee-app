from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.name

      
