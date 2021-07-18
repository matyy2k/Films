from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'premiere', 'year', 'poster', 'imdbRating']

class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czasTrwania', 'gatunek']


class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['stars', 'recenzja']