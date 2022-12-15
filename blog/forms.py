from django.forms import CharField, EmailField, ModelForm, TextInput, EmailInput, Textarea

from .models import Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'enter your name.....'
            }
        ),
        max_length=64
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email'
            }
        ),
        max_length=254
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'style': 'height: 12rem',
                'placeholder': 'Message'

            }
        ),
        max_length=1024
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
