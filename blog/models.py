from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=20)
    title =models.CharField(max_length=20)
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title