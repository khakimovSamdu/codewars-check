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
    
class Lesson(models.Model):
    pass

