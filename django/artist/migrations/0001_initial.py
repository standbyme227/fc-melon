# Generated by Django 2.0.2 on 2018-02-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='artist', verbose_name='프로필 이미지')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('real_name', models.CharField(blank=True, max_length=30, verbose_name='본명')),
                ('nationality', models.CharField(blank=True, max_length=50, verbose_name='국적')),
                ('birth_date', models.DateField(blank=True, max_length=50, null=True)),
                ('constellation', models.CharField(blank=True, max_length=30, null=True, verbose_name='별자리')),
                ('blood_type', models.CharField(blank=True, max_length=50, verbose_name='혈액형')),
                ('intro', models.TextField(blank=True, verbose_name='소개')),
            ],
        ),
    ]
