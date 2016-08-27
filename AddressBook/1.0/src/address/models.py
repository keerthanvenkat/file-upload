from django.db import models

# Create your models here.

class Address(models.Model):
	name = models.CharField(max_length=10)
	email = models.EmailField(max_length=20,primary_key=True)
	age = models.IntegerField(null=True,blank=True)

	def __unicode__(self):
		return u' %s %s %s' %(self.name,self.email,self.age)

class Location(models.Model):
	email = models.ForeignKey(Address)
	location = models.CharField(max_length=30)

	def __unicode__(self):
		return u' %s ' %(self.location)

# https://docs.djangoproject.com/en/1.8/topics/db/models/



