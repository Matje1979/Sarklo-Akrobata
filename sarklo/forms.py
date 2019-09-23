from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Oglas, Post

class OglasCreateForm(forms.ModelForm):
    
    slika = forms.FileField()
    naslov = forms.CharField(max_length = 100)
    
    stanje = forms.CharField(max_length = 100)
    
    cena = forms.IntegerField()
    opis = forms.CharField(widget=forms.Textarea)
    #kategorija = forms.ChoiceField(choices = [('pitanje', 'Pitanje'), ('drugo', 'Drugo')])
    #predmet = forms.CharField(required=False)
   # tekst = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Oglas
        fields = ['slika', 'naslov', 'stanje', 'cena', 'opis']

#post = komentar
class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = ['content']
    