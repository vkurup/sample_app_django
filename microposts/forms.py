from django import forms
from models import Micropost

class MicropostForm(forms.ModelForm):
    class Meta:
        model = Micropost

