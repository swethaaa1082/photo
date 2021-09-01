from .models import photo
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=photo
        fields=['name','desc','img']