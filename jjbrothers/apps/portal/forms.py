from django import forms

from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    sender = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(attrs={
            'class': 'span6'
        })
    )
    subject = forms.CharField(
        label=_('Sujet'),
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'span6'
        })
    )
    message = forms.CharField(
        label=_('Message'),
        widget=forms.Textarea(attrs={
            'class': 'span6'
        })
    )
    #cc_myself = forms.BooleanField(required=False)
