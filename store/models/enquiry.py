from django.db import models


class Enquiry(models.Model):
    custname = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    message = models.CharField(max_length=250)
