from django import forms
from .models import DataItem, Media

class DataItemForm(forms.ModelForm):
    class Meta:
        model = DataItem
        fields = ['title', 'type', 'place_map_1', 'place_map_2', 'img']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'place_map_1': forms.TextInput(attrs={'class': 'form-control'}),
            'place_map_2': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['file', 'media_type']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'media_type': forms.Select(choices=Media.MEDIA_TYPE_CHOICES, attrs={'class': 'form-control'}),
        }

MediaFormSet = forms.formset_factory(MediaForm, extra=0, can_delete=True)
