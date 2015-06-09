import pandas as pd
import sqlite3

db = sqlite3.connect("movieratings/db.sqlite3")
db.execute("DELETE FROM movies_rater")
db.execute("DELETE FROM movies_movie")
db.execute("DELETE FROM movies_rating")

raters = pd.read_csv("data/ml-1m/users.dat", sep="::", header=None,
                     names=["id", "gender", "age", "occupation", "zip_code"])
raters.drop(["gender", "occupation"], axis=1, inplace=True)
raters.to_sql("movies_rater", db, if_exists="append", index=False)

movies = pd.read_csv("data/ml-1m/movies.dat", sep="::", header=None,
                     names=["id", "title", "genres"])
movies.drop(["genres"], axis=1, inplace=True)
movies.to_sql("movies_movie", db, if_exists="append", index=False)

ratings = pd.read_csv("data/ml-1m/ratings.dat", sep="::", header=None,
                      names=["rater_id", "movie_id", "rating", "timestamp"])
ratings.drop(["timestamp"], axis=1, inplace=True)
ratings.to_sql("movies_rating", db, if_exists="append", index=False)