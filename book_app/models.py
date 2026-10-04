from django.db import models
from author_app.models import Author
from genre_app.models import Genre

# Create your models here.

class Books(models.Model):
    title=models.CharField(max_length=100, null=False, blank=False)
    isbn=models.CharField(max_length=20, null=False, blank=False)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    genre=models.ManyToManyField(Genre)
    published_date=models.DateField(null=False, blank=False)


    def __str__(self):
        return f"-{self:title}, -{self:isbn}"
    
    