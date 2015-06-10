from movies.models import Movie, Rating, Rater
import random
from faker import Factory

fake = Factory.create()

def seed_users_movies():

    for num in range(1, 100):
        def random_sex():
            if random.randint(1, 2) == 1:
                return "M"
            else:
                return "F"
        age = random.randint(18, 100)
        occupation = random.randint(0,20)
        new_rater = Rater(num, random_sex(), age, occupation)
        new_rater.save()

        movie_name = fake.name()
        movie_genre = fake.bs()
        new_movie = Movie(num, movie_name, movie_genre)
        new_movie.save()

def seed_ratings():
    raters = Rater.objects.all()
    movies = Movie.objects.all()

    rating_id = 1
    for movie in movies:
        for num in range(20):
            random_rater = raters[random.randint(0, len(raters)-1)]
            rating = random.randint(1, 5)
            date = fake.date_time()
            new_rating = Rating(rating_id, random_rater.pk, movie.pk, date, rating)
            new_rating.save()
            rating_id += 1
