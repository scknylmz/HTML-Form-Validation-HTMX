from django import forms
from django.urls import reverse_lazy


class SimpleForm(forms.Form):
    name = forms.CharField(required=True, 
                            widget=forms.TextInput(
                                attrs={
                                    'hx-get' : reverse_lazy('check-name'),
                                    'hx-target' : '#id-name-error',
                                    'hx-triger' : 'keyup changed delay:1s',
                                    'hx-include': '[name="email"], [name="password"]'
                                }))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(
                                attrs={
                                    'hx-get' : reverse_lazy('check-email'),
                                    'hx-target' : '#id-email-error',
                                    'hx-triger' : 'keyup changed delay:1s',
                                    'hx-include': '[name="name"], [name="password"]'
                                }))
    password = forms.CharField(required=True,
                            widget=forms.PasswordInput(
                                attrs={
                                    'hx-get' : reverse_lazy('check-password'),
                                    'hx-target' : '#id-password-error',
                                    'hx-triger' : 'keyup changed delay:1s',
                                    'hx-include': '[name="email"], [name="name"]'
                                }))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Your Name Is Too Short')
        elif not name.isalpha():
            raise forms.ValidationError('Your Name Can Not Contains Number')
        return name
    