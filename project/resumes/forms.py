from django import forms
from django.contrib.auth.forms import UserCreationForm

import resumes.models
from resumes.models import Resume

# class ResumeCreatingForm(UserCreationForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя'
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите фамилию'
#     }))
#     price = forms.IntegerField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите цену за час занятия'
#     }))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=True)
#     riding_style = forms.ChoiceField(choices=Resume.objects.get())
#
#     class Meta:
#         model = Resume
#         fields = ('first_name', 'last_name', 'description', 'price', 'image', 'riding_style')
