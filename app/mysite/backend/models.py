from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField('title', max_length=50)

    
class Criteria(models.Model):
    title = models.CharField('title', max_length=50)
    count = models.IntegerField('count', default=0)

class Teacher(models.Model):
    name = models.CharField('name', max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')
    lessons_amount = models.IntegerField('lessons_amount')
    courses_amount = models.IntegerField('courses_amount')
    reviews_amount = models.IntegerField('reviews_amount', default=0)
    average = models.FloatField('average')
    total = models.FloatField('total')

class Period(models.Model):
    title = models.CharField('title', max_length=200)
    lessons_amount = models.IntegerField('lessons_amount')
    courses_amount = models.IntegerField('courses_amount')
    reviews_amount = models.IntegerField('reviews_amount', default=0)
    average = models.FloatField('average')


    
