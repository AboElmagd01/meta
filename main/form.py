from django import forms

class Dateform(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget,label="date")
