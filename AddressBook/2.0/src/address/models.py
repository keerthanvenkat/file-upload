from django.db import models


# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,primary_key=True)
    age   = models.IntegerField(null=True,blank=True)


    def __unicode__(self):
        return '%s' %(self.name)

