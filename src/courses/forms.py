from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]

    # field validation form, def clean_<fieldname>
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.isdigit():
            raise forms.ValidationError('this is not valid title')
        return title