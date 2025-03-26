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
    lessons_amount = models.IntegerField('lessons_amount', default=0)
    courses_amount = models.IntegerField('courses_amount', default=0)
    reviews_amount = models.IntegerField('reviews_amount', default=0)
    average = models.FloatField('average', default=0)
    total = models.FloatField('total', default=0)

class Period(models.Model):
    title = models.CharField('title', max_length=200)
    lessons_amount = models.IntegerField('lessons_amount')
    courses_amount = models.IntegerField('courses_amount')
    reviews_amount = models.IntegerField('reviews_amount', default=0)
    average = models.FloatField('average')


    
