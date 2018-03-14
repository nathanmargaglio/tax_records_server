from django.db import models

# Create your models here.

class Record(models.Model):
    street_number = models.IntegerField(default=None, null=True)
    route = models.CharField(default='', max_length=128)
    city = models.CharField(default='', max_length=128)
    county = models.CharField(default='', max_length=128)
    state = models.CharField(default='', max_length=128)

    raw_name = models.CharField(default='', max_length=128)
    first_name = models.CharField(default='', max_length=128)
    last_name = models.CharField(default='', max_length=128)

    link = models.CharField(default='', max_length=128)
    sbl = models.CharField(default='', max_length=128)
    swis = models.CharField(default='', max_length=128)
