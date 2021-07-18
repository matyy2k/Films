from django.db import models

class DodatkoweInfo(models.Model):
    GATUNEK = (
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
    )

    czasTrwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

    def __str__(self):
        return f'Czas trwania: {self.czasTrwania}, Gatunek: {self.get_gatunek_display()}'

class Film(models.Model):
    title = models.CharField(max_length=64)
    year = models.PositiveIntegerField(default=2000)
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imdbRating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titleWithYear()

    def titleWithYear(self):
        return f'{self.title} ({self.year})'

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)

