from django import forms

class nameform(forms.Form):
    name=forms.CharField(max_length=200,)
    age=forms.IntegerField(min_value=18)

