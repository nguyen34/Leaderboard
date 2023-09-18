from django.forms import ModelForm
from django import forms
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'address']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        name = cleaned_data.get('name')
        age = cleaned_data.get('age')
        address = cleaned_data.get('address')

        if not name or not age or not address:
            raise forms.ValidationError('All fields are required!')

        if (type(name) != str or type(age) != int or type(address) != str):
            raise forms.ValidationError('Invalid data types!')

        if (age < 0 or age > 100):
            raise forms.ValidationError('Age must be between 1 and 100!')
        return cleaned_data
