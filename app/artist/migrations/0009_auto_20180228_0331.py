# Generated by Django 2.0.2 on 2018-02-28 03:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0008_auto_20180228_0310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistyoutube',
            old_name='url_img_cover',
            new_name='url_thumbnail',
        ),
        migrations.AlterField(
            model_name='artist',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_artists', through='artist.ArtistLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
