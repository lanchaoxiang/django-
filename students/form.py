from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError("必须是数字")
        return int(cleaned_data)
    class Meta:
        model = Students
        fields =('name','sex','profession','phone','email')