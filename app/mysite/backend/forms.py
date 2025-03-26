from .models import Teacher, Criteria

from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'lessons_amount', 'courses_amount', 'average']

class CriteriaForm(ModelForm):
    class Meta:
        model = Criteria
        fields = ['title']
