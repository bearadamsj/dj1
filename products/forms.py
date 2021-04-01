from django import forms
from .models import Product

class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = [
            'num_of_shift',
            'num_of_defective_parts',
            'description'
        ]

class RawProductForm(forms.Form):
    num_of_shift = forms.CharField(label='number of shifts', widget=forms.TextInput(attrs={'placeholer': 'yours'}))
    num_of_defective_parts = forms.CharField()
    description = forms.DecimalField()
