from django import forms


class ReceiptUidManual(forms.Form):
	receipt_uid = forms.CharField(label='UID',  widget=forms.TextInput(attrs={'placeholder': 'O-3C2BE10AC9C84D98ABE10AC9C84D98AB', 'class':'form-control'}))