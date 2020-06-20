from django.db import models
from system.models import Student, Professor


class Proposal(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
