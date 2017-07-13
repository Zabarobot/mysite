from django import forms
from .models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            "name",
            "email",
            "message"
        ]


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        data = self.cleaned_data['name']  #clean_data - bierze 'dobre' dane przetworzone przez poprzednie funkcje walidujace
        if "D" not in data:
            raise forms.ValidationError("Musisz miec imie zawierajace 'D'!")
