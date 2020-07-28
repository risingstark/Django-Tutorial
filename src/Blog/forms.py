from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description = forms.Charfield(lable='', widget=forms.TexInput(attrs={"placeholder":"your description"}))
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'feature'
        ]
