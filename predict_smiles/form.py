from django import forms

class SmilesForm(forms.Form):
    MW = forms.FloatField(label="MW", widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    LogP = forms.FloatField(label="LogP", widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    TPSA = forms.FloatField(label="TPSA", widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
