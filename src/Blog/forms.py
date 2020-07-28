from django import forms

from .models import Article

class BlogForm(forms.ModelForm):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description = forms.CharField(
                                        required=False,
                                        widget=forms.Textarea(
                                        attrs={
                                                "placeholder":"your description",
                                                "class":"New-Class-name two",
                                                "id" : "my-id-for-textarea",
                                                "rows" :20,
                                                "cols" :20
                                        }
                                    )
                                )

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'feature'
        ]
