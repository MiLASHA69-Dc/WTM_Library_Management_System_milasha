from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    GENDER = (
        ("Male","male"),
        ("Female","female")
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=6,choices=GENDER,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    country=models.CharField(max_length=40,blank=True,null=True)
    city=models.CharField(max_length=40,blank=True,null=True)

    def __str__(self):
        return f"{self.user}"