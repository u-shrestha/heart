from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from .models import Heart, Register
from .forms import Heart_form
from predict import predict
from .forms import UserLoginForm, UserRegisterForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout

# Create your views here.
fin = []

def index(request):
    form = Heart_form()

    if request.method == 'POST':
        form = Heart_form(request.POST)
        data = request.POST

        age = data.__getitem__('age')
        fin.append(age)

        sex = data.__getitem__('sex')
        fin.append(sex)

        chest_pain_type = data.__getitem__('chest_pain_type')
        fin.append(chest_pain_type)

        resting_bloodpressure = data.__getitem__('resting_bloodpressure')
        fin.append(resting_bloodpressure)

        serum_cholestrol = data.__getitem__('serum_cholestrol')
        fin.append(serum_cholestrol)

        fasting_blood_sugar = data.__getitem__('fasting_blood_sugar')
        fin.append(fasting_blood_sugar)

        resting_ecg = data.__getitem__('resting_ecg')
        fin.append(resting_ecg)

        max_heartrate = data.__getitem__('max_heartrate')
        fin.append(max_heartrate)

        exercise_induced_angina = data.__getitem__('exercise_induced_angina')
        fin.append(exercise_induced_angina)

        oldpeak = data.__getitem__('oldpeak')
        fin.append(oldpeak)

        slope = data.__getitem__('slope')
        fin.append(slope)

        no_of_major_vessel = data.__getitem__('no_of_major_vessel')
        fin.append(no_of_major_vessel)

        thalassemia = data.__getitem__('thalassemia')
        fin.append(thalassemia)

        if form.is_valid():
            print(fin)
            form.save(commit=True)
            result = heart_predict(request)
            fin.clear()
            return result
        else:
            print(fin)
            print("Form validation failed")


    return render(request, "prediction/predict.html", {'form': form})



def heart_predict(request):
    val = predict.predict(fin)
    return render(request, "prediction/result.html", {'fin': val})



def login_view(request):
    if request.user.is_authenticated:
        return render(request, "prediction/dashboard.html")

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')

    elif form.errors:
        messages.error(request, 'username or password incorrect')
        form = UserLoginForm()

    context = {'form': form}
    return render(request, "prediction/login.html", context)



def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        userObj = form.cleaned_data
        username = userObj['username']
        email_address = userObj['email_address']
        password = userObj['password']
        confirm_password = userObj['confirm_password']
        date_of_birth = userObj['date_of_birth']
        gender = userObj['gender']

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email_address).exists()):
            new_user = Register.objects.create(username= username, email_address= email_address,
                                               password=password, confirm_password=confirm_password,
                                               date_of_birth=date_of_birth, gender=gender)
            new_user.save()

            login(request, User.objects.create_user(username, email_address, password))
            return redirect('dashboard')
        else:
            raise forms.ValidationError("username or email already exists")

    elif form.errors:
        form = UserRegisterForm()

    context = {'form': form }
    return render(request, "prediction/signup.html", context)


def dashboard(request):
    return render(request, 'prediction/dashboard.html')

def history(request):
    history_list = Heart.objects.all()
    context = {'history_list': history_list }
    return render(request, 'prediction/history.html', context)


def history_detail(request,id):
    data=get_object_or_404(Heart,id=id)
    context={
        'data':data,
    }
    return render(request,'prediction/historyDetail.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')


def user(request):
    list = Register.objects.all()
    return render(request, 'prediction/user_detail.html', {'list':list})