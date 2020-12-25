from django.db import models

# Create your models here.
class Journal(models.Model):
    journalname = models.CharField(max_length=250)
    editor = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.text
