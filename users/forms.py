from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TimeInput(attrs={'class' : 'form-control', 'placeholder' : 'write a title'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'write a description'})
        }