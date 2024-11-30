from django import forms
import datetime

from authors.models import Author

class AuthorForm(forms.ModelForm):

    birthdate = forms.DateField(
widget=forms.DateInput(attrs={'type': 'date'}),
label="Date de naissance"
)
    class Meta:
        model = Author
        fields = ['name', 'birthdate', 'biography', 'image']