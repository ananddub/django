from django.db import models

class Student(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    password = models.CharField(max_length=30,default="12345")
    admission_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    def __str__(self):
        return self.name
