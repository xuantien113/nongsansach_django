from django import forms
from django.forms import TextInput, Textarea


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    productid = forms.IntegerField()