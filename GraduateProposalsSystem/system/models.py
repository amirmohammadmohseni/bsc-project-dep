from django.db import models

class BaseUser(models.Model):
    name = models.CharField(max_length=200)

class Student(models.Model):
    student_id = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Professor(models.Model):
    professor_id = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)