from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    email = forms.CharField(label='Email', max_length=50)
    message = forms.CharField(label='Message', max_length=500)
