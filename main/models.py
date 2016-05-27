from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=60)
    message=models.TextField()

    def __unicode__(self):
        return self.subject + ': ' + self.email

class Order(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    city=models.CharField(max_length=60)
    postcode=models.CharField(max_length=60)
    country=models.CharField(max_length=60)
    address=models.CharField(max_length=100)
    hubs=models.IntegerField(default=0)
    ai=models.IntegerField(default=0)

    cardnumber=models.CharField(max_length=16)
    securitynumber=models.CharField(max_length=3)

    def __unicode__(self):
        return self.email + ': ' + self.country

        