from django.forms import ModelForm
from .models import Heart

from django import forms

from django.contrib.auth import (
    authenticate,
    get_user_model

)

gender = (
        ('1', 'Male'),
        ('0', 'Female')
)

User = get_user_model()


class Heart_form(ModelForm):
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


class UserRegisterForm(forms.ModelForm):
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
            'gender'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password mismatch")

        username_qs = User.objects.filter(username=username)
        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")

        if username_qs.exists():
            raise forms.ValidationError("Username already exists")
        return super(UserRegisterForm, self).clean(*args, **kwargs)