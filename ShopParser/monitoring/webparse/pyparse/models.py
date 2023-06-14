from django.db import models

# Create your models here.

class MobilePhone(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    currency = models.CharField(max_length=3)
    date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title
