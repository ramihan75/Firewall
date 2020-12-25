from django.db import models

# Create your models here.
class Book(models.Model):
    bookname = models.CharField(max_length=250)
    authorbook = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.text