import datetime


from django import forms
from django.forms import DateTimeInput
from django.http import request

from resumes.models import Resume, RidingStyle, Record


class ResumeCreatingForm(forms.ModelForm):
    # STYLE_CHOICES = [(-1, 'Выберите')]
    # STYLE_CHOICES += [(style.id, style.name.capitalize()) for style in RidingStyle.objects.all()]
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'
    }))
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите цену за час занятия'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4',
        'style': "resize: vertical; vertical-align: top; height: 4em;",
        'placeholder': 'О себе'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    riding_style = forms.ModelChoiceField(queryset=RidingStyle.objects.all())

    class Meta:
        model = Resume
        fields = ('first_name', 'last_name', 'description', 'price', 'image', 'riding_style')


class OrderCreatingForm(forms.ModelForm):
    fio = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите ФИО'
    }))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите номер'
    }))
    date = forms.DateTimeField(required=False, widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                               initial=datetime.date.today(), localize=True)

    class Meta:
        model = Record
        fields = ('fio', 'phone', 'date', 'instructor')
