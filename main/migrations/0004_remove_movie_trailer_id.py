# Generated by Django 4.2.3 on 2023-07-31 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_movie_trailer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailer_id',
        ),
    ]
