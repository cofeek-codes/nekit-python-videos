from .models import Teacher

from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'lessons_amount', 'courses_amount', 'average', 'total']
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
