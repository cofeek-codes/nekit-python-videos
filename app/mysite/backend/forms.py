from .models import A

from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class AForm(ModelForm):
    class Meta:
        model = A
        fields = ['title', 'anons', 'full_text', 'date']
        # widgets = {
        # "title": TextInput(attrs={
        #     'class': 'send_input',
        #     'placeholder': 'name letter'
        #                    }),

        # "anons": TextInput(attrs={
        #     'class': 'send_input',
        #     'placeholder': 'about letter'
        #                    }),
        # "date": TextInput(attrs={
        #     'class': 'send_input',
        #     'placeholder': 'date'
        #                    }),

        # "full_text": Textarea(attrs={
        #     'class': 'send_input',
        #     'placeholder': 'text letter'
        #                    }),

        # }
