# Generated by Django 3.2.5 on 2021-07-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_auto_20210718_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (1, 'Horror'), (2, 'Komedia'), (3, 'Sci-fi'), (4, 'Drama')], default=0),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='filmyweb.Film')),
            ],
        ),
    ]
