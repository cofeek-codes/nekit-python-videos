from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField('name', max_length=200)
    subject = models.CharField('subject', max_length=50)
    lessons_amount = models.IntegerField('lessons_amount')
    courses_amount = models.IntegerField('courses_amount')
    average = models.FloatField('average')
    total = models.FloatField('total')
    
