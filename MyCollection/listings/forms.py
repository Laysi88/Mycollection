from django import forms
from . import models


class BookForm(forms.ModelForm):
    price = forms.DecimalField(label="Prix", required=False)
    author = forms.CharField(label="Auteur", required=False)
    picture = forms.ImageField(label="Images", required=False)

    class Meta:
        model = models.Book
        fields = ["name", "genre", "price", "author", "picture"]
        labels = {
            "name": "Titre",
        }
