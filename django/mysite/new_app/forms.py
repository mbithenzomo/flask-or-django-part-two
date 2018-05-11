from django import forms

from .models import User


class ContactForm(forms.Form):
    email = forms.EmailField(label='Your Email Address', required=True)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Your Message', required=True)


class SignUpForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ('email', 'username', 'first_name', 'last_name')
