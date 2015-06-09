# Django Movie Ratings

## Description

Create an interface in Django to the [MovieLens dataset][movielens].

## Learning Objectives

After completing this assignment, you should be able to:

* Create a new Django application
* Translate real-world data to Django models
* Explain what a database is
* Explain what a model is
* Use the Django admin
* Structure the Django admin to reflect your data

## Details

### Deliverables

* A Git repo called django-movies containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called `movieratings`

## Normal Mode

Choose a dataset from the [MovieLens dataset options][movielens] and read its
README.

Create a new Django application in the `movieratings` project to hold your
models.

Create Django models for users (call the model `Rater` so as not to
confuse it with Django users), movies, and ratings. Make sure that your models
can contain the data from your dataset.

Create Django admin pages for your models. From the rater page, you should
be able to see all their ratings and add new ratings. From the movie page,
you should be able to see all ratings as well.

[movielens]: http://grouplens.org/datasets/movielens/
