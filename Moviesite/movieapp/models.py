from django.db import models

# Create your models here.
class Movie(models.Model):
	title=models.CharField(max_length=200)
	origin=models.CharField(max_length=200)
	url=models.CharField(max_length=200)
	rating=models.CharField(max_length=200)
	image=models.CharField(max_length=200)
	directors =models.CharField(max_length=200)
	casts=models.CharField(max_length=200)
	year=models.CharField(max_length=200)
	genres=models.CharField(max_length=200)
	countries=models.CharField(max_length=200)
	summary=models.CharField(max_length=200)
	def __unicode__(self):
		return self.title
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
