from django.db import models

# Create your models here.

class Genre(models.Model):
    title=models.CharField(max_length=100, null=False, blank=False)
    category=models.CharField(max_length=100, null=False, blank=False)

    
    def __str__(self):
        return f"{self.title} - {self.category}" 