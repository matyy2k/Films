# Generated by Django 3.2.5 on 2021-07-18 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0004_auto_20210718_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (4, 'Drama'), (3, 'Sci-fi'), (2, 'Komedia'), (1, 'Horror')], default=0),
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recenzja', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmyweb.film')),
            ],
        ),
    ]
