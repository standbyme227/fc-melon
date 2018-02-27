from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Album
from django import forms

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'img_cover',
            'release_date',
        ]
    #widget 추가가능