# Generated by Django 2.0.2 on 2018-02-27 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_auto_20180226_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songlike',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user_info_list', to='song.Song'),
        ),
        migrations.AlterField(
            model_name='songlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_song_info_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
