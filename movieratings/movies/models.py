from django.db import models

# Create your models here.

class Rater(models.Model):
    age = models.IntegerField()
    zip_code = models.CharField(max_length=10)

class Movie(models.Model):
    title = models.CharField(max_length=255)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()