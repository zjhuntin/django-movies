from django.db import models
from statistics import mean
from math import sqrt


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

    def __str__(self):
        return "User {}, {}, {}".format(self.pk, self.gender, occupations[self.occupation])

    @property
    def average_rating(self):
        return mean([rating.rating for rating in self.rating_set.all()])

    def compare_ratings(self, other_rater):
        rater_ratings = self.rating_set.all()
        other_ratings = other_rater.rating_set.all()
        def get_movie_set(rater_ratings, other_ratings):
            rater_movies = {rating.movie for rating in rater_ratings}
            other_movies = {rating.movie for rating in other_ratings}
            return rater_movies & other_movies
        movie_set = get_movie_set(rater_ratings, other_ratings)
        rater_ratings = [rating for rating in rater_ratings if rating.movie in movie_set]
        others_ratings = [rating for rating in other_ratings if rating.movie in movie_set]
        difference = [(rater_ratings[idx].rating - others_ratings[idx].rating) for idx in range(len(movie_set))]
        sum_squares = sum([num ** 2 for num in difference])
        return 1 / (1 + sqrt(sum_squares))


    def best_unseen(self, number_wanted):
        seen_movies = [rating.movie for rating in self.rating_set.all()]
        best_movies = top_movies(number_wanted)
        best_not_seen = []
        for movie in best_movies:
            if movie not in seen_movies:
                best_not_seen.append(movie)
        return best_not_seen


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        self.rating_set.all()
        return mean([rating.rating for rating in self.rating_set.all()])


def top_movies(number_wanted):
    top_movies = Movie.objects.all()
    top_movies = sorted(top_movies, key=lambda movie: movie.average_rating, reverse=True)
    return top_movies[:number_wanted:]


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    timestamp = models.DateTimeField()
    rating = models.IntegerField()

    def __str__(self):
        return "{} rating for {} is {}".format(self.rater, self.movie, self.rating)
