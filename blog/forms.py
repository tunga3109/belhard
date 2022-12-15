from django.forms import CharField, EmailField, Form, TextInput, EmailInput, Textarea


class ContactForm(Form):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'enter your name.....'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email'
            }
        )
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'style': 'height: 12rem',
                'placeholder': 'Message'

            }
        )
    )
