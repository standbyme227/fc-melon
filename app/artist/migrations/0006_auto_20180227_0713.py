# Generated by Django 2.0.2 on 2018-02-27 07:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0005_auto_20180227_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_artists', through='artist.ArtistLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
