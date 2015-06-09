from django.contrib import admin

# Register your models here.

from .models import Rater, Movie, Rating

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    fields = ["title"]
    list_display = ["title", "average_rating"]

admin.site.register(Rater)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)