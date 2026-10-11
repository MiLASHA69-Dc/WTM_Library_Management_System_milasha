from django.db import models

# Create your models here.

class Genre(models.Model):
    CHOICES = (
        ("Fiction","Action & Adventure"),
        ("Fiction","Alternative History"),
        ("Fiction","Anthology"),
        ("Fiction","Children's Fiction"),
        ("Fiction","Classic Literature"),
        ("Fiction","Commercial Fiction"),
        ("Fiction","Contemporary Fiction"),
        ("Fiction","Cozy Mystery"),
        ("Fiction","Crime Fiction"),
        ("Fiction","Cyberpunk"),
    )
    title=models.CharField(max_length=100, null=False, blank=False)
    category=models.CharField(max_length=100, choices=CHOICES, null=False, blank=False)

    
    def __str__(self):
        return f"{self.title}" 