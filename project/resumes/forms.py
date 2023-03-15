from django import forms

import resumes.models
from resumes.models import Resume, RidingStyle


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
    # riding_style = forms.ChoiceField(label='Style', choices=STYLE_CHOICES)

    riding_style = forms.ModelChoiceField(queryset=RidingStyle.objects.all())

    # riding_style = forms.ChoiceField(widget=forms.RadioSelect,
    #                                  choices=[(style.name, style) for style in RidingStyle.objects.filter()]
    #                                  )

    class Meta:
        model = Resume
        fields = ('first_name', 'last_name', 'description', 'price', 'image', 'riding_style')
