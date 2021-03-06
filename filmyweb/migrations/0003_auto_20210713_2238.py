# Generated by Django 3.2.5 on 2021-07-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0002_film_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='imdbRating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
    ]
