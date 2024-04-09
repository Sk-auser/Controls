from django import forms
class NumberForm(forms.Form):
    number = forms.FloatField(label='Enter a number', min_value=0)