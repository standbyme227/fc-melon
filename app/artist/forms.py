from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Artist
from django import forms

__all__ = (
    'ArtistForm'
)

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['image',
                  'name',
                  'real_name',
                  'nationality',
                  'birth_date',
                  'constellation',
                  'blood_type',
                  'intro']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


        # def clean_melon_id(self):
        #     melon_id = self.cleaned_data['melon_id']
        #     # if Artist.objects.filter(malon_id=data).exists():
        #     #     raise ValidationError('이미 등록된 사용자입니다.')
        #     return melon_id
        #
        # def clean_name(self):
        #     name = self.cleaned_data['name']
        #     return name
        #
        # def clean_real_name(self):
        #     real_name = self.cleaned_data['real_name']
        #     return real_name
        #
        # def clean_blood_type(self):
        #     blood_type = self.cleaned_data['blood_type']
        #     return blood_type
        #
        # def clean_birth_date(self):
        #     birth_date = self.cleaned_data['birth_date']
        #     return birth_date


        # def nationality(self):
        #     name = self.cleaned_data['name']
        #     return name
        #
        # def clean_name(self):
        #     name = self.cleaned_data['name']
        #     return name
        #
        # def clean_name(self):
        #     name = self.cleaned_data['name']
        #     return name
        #
        # def clean_name(self):
        #     name = self.cleaned_data['name']
        #     return name