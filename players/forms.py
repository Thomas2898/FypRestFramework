from django import forms

from players.models import Player

class HomeForm(forms.Form):
    name = forms.CharField(max_length=50)
    lon = forms.FloatField()
    lat = forms.FloatField()