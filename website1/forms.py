from django import forms
from django.forms import TextInput

class Usersform(forms.Form):
    num1 = forms.CharField(label="Number1", widget=forms.TextInput(attrs={"class": "form-control"}))
    num2 = forms.CharField(label="Number2", widget=forms.TextInput(attrs={"class": "form-control"}))
    CHOICES = [("1", "addition"), ("2", "Substraction"), ("3", "Multiplication"), ("4", "Division")]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    