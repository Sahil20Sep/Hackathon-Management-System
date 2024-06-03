from django import forms
from .models import ParticipantModel, HackathonModel

class Participantforms(forms.ModelForm):
    class Meta:
        model=ParticipantModel
        fields="__all__"

class Hackathonforms(forms.ModelForm):
    class Meta:
        model=HackathonModel
        fields="__all__"
