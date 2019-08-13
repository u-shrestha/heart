from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Heart
from home.models import Doctor, Hospital, Register
from django import forms
from .forms import Heart_form, UserLoginForm, UserRegisterForm
from predict import predict
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.db.models import Q
from itertools import chain

# Create your views here.
fin = []


@login_required
def index(request):
    form = Heart_form()
    # name = request.user

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
            fs = form.save(commit=False)
            fs.name = request.user.username
            fs.save()
            result = heart_predict(request)
            fin.clear()
            return result
        else:
            print("Form validation failed")

    return render(request, "prediction/predict.html", {'form': form })



def heart_predict(request):
    val = predict.predict(fin)
    return render(request, "prediction/result.html", {'fin': val})


# view for user login
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


# view for user registration
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
            #saving the data of new user in database
            new_user = Register.objects.create(username= username, email_address= email_address,
                                               password=password, confirm_password=confirm_password,
                                               date_of_birth=date_of_birth, gender=gender)

            new_user.save()

            # email confirmation
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('prediction/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email_address')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            # login after sign up
            # login(request, User.objects.create_user(username, email_address, password))
            # return redirect('dashboard')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
            elif User.objects.filter(email=email_address).exists():
                messages.error(request, 'email already exists')
            form = UserRegisterForm()

    elif form.errors:
        messages.error(request, 'username already exists')
        form = UserRegisterForm()

    context = {'form': form }
    return render(request, "prediction/signup.html", context)


# proceed to confirm/activate email
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.set_password(user.password)
        user.save()
        login(request, user)
        return redirect('dashboard')
    else:
        return HttpResponse('Activation link is invalid!')


#view for changing current password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # retriving username and new passwords to update it in model
            username_user = str(User.objects.filter(username=request.user).get())
            username_register = str(Register.objects.filter(username=username_user).get())
            userObj = form.cleaned_data
            password = userObj['new_password1']
            confirm_password = userObj['new_password2']

            user = form.save()
            update_session_auth_hash(request, user)  # Important!

            #updating the passwords in models
            if (username_user == username_register):
                Register.objects.update(password=password, confirm_password=confirm_password)

            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'prediction/change_password.html', {'form': form })


def dashboard(request):
    return render(request, 'prediction/dashboard.html')


def search(request):
    if request.method == 'POST':
        srch = request.POST['q']
        if srch:
            match = list(chain(Hospital.objects.filter(Q(name__icontains=srch) | Q(location__icontains=srch)),
                               Doctor.objects.filter(Q(name__icontains=srch))))
            if match:
                return render(request, 'prediction/search.html', {'search_result_list': match, 'search_count': len(match) , 'search_word': srch })

            else:
                messages.error(request, 'No result found.')
        else:
            return redirect('home')

    return render(request, 'prediction/search.html')


def history(request):
    history_list = Heart.objects.all()
    context = {'history_list': history_list }
    return render(request, 'prediction/history.html', context)


def history_detail(request, id):
    data=get_object_or_404(Heart, id=id)
    context={'data':data }
    return render(request, 'prediction/history_detail.html', context)

# logout user
def logout_view(request):
    logout(request)
    return redirect('login')


def attribute(request):
    return render(request, 'prediction/attribute.html')


def user(request, user_id):
    list = Register.objects.filter(id=user_id)
    user = User.objects.all()
    # list = Register.objects.filter(pk=user_id)
    return render(request, 'prediction/user_detail.html', {'list':list, 'user':user})




