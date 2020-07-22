from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

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
