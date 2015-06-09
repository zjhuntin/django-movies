from django.db import models

occupations = {0: "Other",
               1: "academic",
               2: "artist",
               3: "Clerical/admin",
               4: "college/grad student",
               5: "customer service",
               6: "doctor/health care",
               7: "executive/managerial",
               8: "farmer",
               9: "homemaker",
               10: "K-12 student",
               11: "lawyer",
               12: "programmer",
               13: "retired",
               14: "sales/marketing",
               15: "scientist",
               16: "self-employed",
               17: "technician/engineer",
               18: "tradesman/craftersman",
               19: "unemployed",
               20: "writer"}

class Rater(models.Model):
    gender = models.CharField(max_length=2)
    age = models.IntegerField()
    occupation = models.IntegerField()

    def __str__():
        return "User {}, {}, {}".format(self.pk, self.gender, occupations[self.occupation])

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__():
        return self.title

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    timestamp = models.DateField()
    rating = models.IntegerField()

    def __str__():
        return "{} rating for {} is {}".format(self.rater, self.movie, self.rating)
