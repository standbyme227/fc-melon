# Generated by Django 2.0.2 on 2018-02-08 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default=2, max_length=100, verbose_name='장르'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, verbose_name='가사'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50, verbose_name='곡 제목'),
        ),
    ]
