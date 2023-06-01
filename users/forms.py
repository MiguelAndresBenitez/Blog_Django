from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="Ingrese el titulo", max_length=200)
    content = forms.CharField(label='Ingrese el contenido', widget=forms.Textarea)