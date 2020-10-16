from django.db import models


# Create your models here.

class Transaction(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    due = models.DateField()

    def __str__(self):
        return self.title
