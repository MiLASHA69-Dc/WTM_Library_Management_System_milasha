from django.db import models
from author_app.models import Author
from genre_app.models import Genre
#from accounts.models import User
from django.contrib.auth import get_user_model



# Create your models here.

User=get_user_model()

class Book(models.Model):

    Choices=(
        ("av","Available"),
        ("br","Borrowed"),
        )
    
    title=models.CharField(max_length=100, null=False, blank=False)
    isbn=models.CharField(max_length=20, null=False, blank=False)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    genre=models.ManyToManyField(Genre)
    status=models.CharField(max_length=20, choices=Choices,default='av',blank=True,null=True)
    published_date=models.DateField(null=False, blank=False)

    
    
    def __str__(self):
        return f"{self.title}"
    
class BookRequest (models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    date_of_request = models.DateField(null=False,blank=False)
    date_of_return = models.DateField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book}"