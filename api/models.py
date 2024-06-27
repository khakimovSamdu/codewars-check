from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=125)
    
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    usrename = models.CharField(max_length=125)
    name = models.CharField(max_length=125)
    guruh = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Mavzu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    id = models.CharField(max_length=123, primary_key=True)
    name = models.CharField(max_length=255)
    mavzu = models.ForeignKey(Mavzu, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

