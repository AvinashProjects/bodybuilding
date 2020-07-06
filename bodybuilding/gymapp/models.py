from django.db import models

# Create your models here.

class Member(models.Model):
    name=models.CharField(max_length=64)
    phone=models.CharField(max_length=10)
    plan=models.CharField(max_length=64)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name

class Plan(models.Model):
    name=models.CharField(max_length=64)
    amount=models.CharField(max_length=64)
    duration=models.CharField(max_length=64)

    def __str__(self):
        return self.name

