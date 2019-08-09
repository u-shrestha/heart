from django.forms import ModelForm
from .models import Heart, Register
from django.core.exceptions import ValidationError
from django import forms
from django.db import models
from django.contrib.auth import authenticate, get_user_model

gender = [
        ('1', 'Male'),
        ('0', 'Female')
]

chest_pain_type_choice = [
    ('1', 'typical angina'),
    ('2', 'atypical angina'),
    ('3', 'non-anginal pain'),
    ('4', 'asymptotic')
]

fasting_blood_sugar_choice = [
    ('1', 'True'),
    ('0', 'False')
]

resting_ecg_choice = [
    ('0', 'normal'),
    ('1', 'ST-T wave abnormality'),
    ('2', 'left ventricular hyperthrophy')
]

exercise_induced_angina_choice = [
    ('1', 'Yes'),
    ('0', 'No')
]

slope_choice = [
    ('1', 'upsloping'),
    ('2', 'flat'),
    ('3', 'downsloping')
]

thalassemia_choice = [
    ('3', 'normal'),
    ('6', 'fixed defect'),
    ('7', 'reversable defect')
]

User = get_user_model()


class Heart_form(ModelForm):
    chest_pain_type = forms.ChoiceField(widget=forms.Select, choices=chest_pain_type_choice)
    fasting_blood_sugar = forms.ChoiceField(widget=forms.Select, choices=fasting_blood_sugar_choice)
    resting_ecg = forms.ChoiceField(widget=forms.Select, choices=resting_ecg_choice)
    exercise_induced_angina = forms.ChoiceField(widget=forms.Select, choices=exercise_induced_angina_choice)
    slope = forms.ChoiceField(widget=forms.Select, choices=slope_choice)
    thalassemia = forms.ChoiceField(widget=forms.Select, choices=thalassemia_choice)

    class Meta:
        model = Heart
        fields = '__all__'


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(ModelForm):
    username = forms.CharField(max_length=50)
    email_address = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender)

    class Meta:
        model = User
        fields = [
            'username',
            'email_address',
            'password',
            'confirm_password',
            'date_of_birth',
            'gender',
        ]