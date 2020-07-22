from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"}))
    email       = forms.EmailField()
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
                        ) # required  = True is default
    price       = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "h" in title:
            raise forms.ValidationError("this is not a valid title")
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not "@" in email:
            raise forms.ValidationError("this is not a valid title")
        else:
            return email

class RawProductForm(forms.Form):

    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"})) # required = True is default
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
                        ) # required  = True is default
    price       = forms.DecimalField(initial=199.99)
