from django.contrib import admin
from .models import *

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ['title', 'year', 'description']
    #exclude = ['description']
    list_display = ['title', 'imdbRating', 'year']
    list_filter = ['year', 'imdbRating']
    search_fields = ['title', 'description']

@admin.register(DodatkoweInfo)
class DodatkoweInfo(admin.ModelAdmin):
    list_display = ['czasTrwania', 'gatunek']

admin.site.register(Ocena)
admin.site.register(Actor)