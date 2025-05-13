from django import forms

class BarcodeScanForm(forms.Form):
    barcode = forms.CharField(
        label="Scan or Enter Barcode",
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'})
    )