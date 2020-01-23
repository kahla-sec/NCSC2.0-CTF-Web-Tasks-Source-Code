from django import forms


class TesterForm(forms.Form):
    Input = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Link To Test'}))
