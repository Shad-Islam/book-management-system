from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    published_year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title