# Generated by Django 4.2.3 on 2023-07-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_id',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
