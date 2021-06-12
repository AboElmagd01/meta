from django import forms

class Dateform(forms.Form):
    fromdate = forms.DateField(widget=forms.SelectDateWidget,label="date")
    todate = forms.DateField(widget=forms.SelectDateWidget,label="date")
