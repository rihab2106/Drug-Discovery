from django import forms

class SmilesForm(forms.Form):
    smile=forms.CharField(label="SMILES", max_length=200, error_messages="SMILES with less than 200 characters")

