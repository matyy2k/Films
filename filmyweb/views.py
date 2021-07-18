from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film, DodatkoweInfo, Ocena
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


def allFilms(request):
    #return HttpResponse('<h1>To jest nasz pierwszy test</h1>')


    all = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': all})

@login_required()
def newFilm(request):
    formFilm = FilmForm(request.POST or None, request.FILES or None)
    formDodatkowe = DodatkoweInfoForm(request.POST or None)
    if all((formFilm.is_valid(), formDodatkowe.is_valid())):
        film = formFilm.save(commit=False)
        dodatkowe = formDodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(allFilms)
    return render(request, 'filmForm.html', {'form': formFilm, 'formDodatkowe': formDodatkowe, 'oceny': None,'formOcena': None, 'nowy': True})

@login_required()
def editFilm(request, id):
    film = get_object_or_404(Film, pk=id)

    oceny = Ocena.objects.filter(film=film)

    try:
        dodatkowe = DodatkoweInfo.objects.get(film=id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    formFilm = FilmForm(request.POST or None, request.FILES or None, instance=film)
    formDodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    formOcena = OcenaForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            ocena = formOcena.save(commit=False)
            ocena.film = film
            ocena.save()

    if all((formFilm.is_valid(), formDodatkowe.is_valid())):
        film = formFilm.save(commit=False)
        dodatkowe = formDodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(allFilms)
    return render(request, 'filmForm.html', {'form': formFilm, 'formDodatkowe': formDodatkowe, 'oceny': oceny,'formOcena': formOcena, 'nowy': False})

@login_required()
def deleteFilm(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(allFilms)

    return render(request, 'confirm.html', {'film': film})

