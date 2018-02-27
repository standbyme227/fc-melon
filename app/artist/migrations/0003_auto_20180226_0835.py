# Generated by Django 2.0.2 on 2018-02-26 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20180226_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_artists', through='artist.ArtistLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artistlike',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user_info_list', to='artist.Artist'),
        ),
        migrations.AlterField(
            model_name='artistlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_artist_info_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
