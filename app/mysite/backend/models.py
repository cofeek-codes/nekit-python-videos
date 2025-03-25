from django.db import models

# Create your models here.

class A(models.Model):
    title = models.CharField('title', max_length=50)
    anons = models.CharField('anons', max_length=50)
    full_text = models.TextField('full text')
    date = models.DateTimeField('publish date')

    def __str__(self):
        return f"News - {self.title}"
    
    def get_absolute_path(self):
        return f"/backend/{self.id}"

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
