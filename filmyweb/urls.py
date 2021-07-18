from django.urls import path
from filmyweb.views import allFilms, newFilm, editFilm, deleteFilm

urlpatterns = [
    path('wszystkie/', allFilms, name='allFilms'),
    path('nowy/', newFilm, name='newFilm'),
    path('edytuj/<int:id>/', editFilm, name='editFilm'),
    path('usun/<int:id>/', deleteFilm, name='deleteFilm'),
]

