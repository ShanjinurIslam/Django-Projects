from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    url = models.URLField()
    date = models.DateField(auto_now=False, auto_now_add=False)