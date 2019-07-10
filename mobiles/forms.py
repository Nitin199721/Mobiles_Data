from django import forms


class InputForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Enter your email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    Url_field = forms.URLField(label='URL', widget=forms.TextInput(attrs={'placeholder': 'Enter Url'}))

