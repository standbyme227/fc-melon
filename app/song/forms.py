from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Song
from django import forms

__all__ = (
    'SongForm'
)


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title',
                  'genre',
                  'lyrics',
                  'album',
                  'artists',
                  ]

        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     )
        # }
