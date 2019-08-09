from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Heart(models.Model):
    name =models.ForeignKey(User, related_name='Heart.name+', on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default=0)
    sex = models.IntegerField(default=0)
    chest_pain_type = models.FloatField(default=0)
    resting_bloodpressure = models.FloatField(default=0)
    serum_cholestrol = models.FloatField(default=0)
    fasting_blood_sugar = models.FloatField(default=0)
    resting_ecg = models.FloatField(default=0)
    max_heartrate = models.FloatField(default=0)
    exercise_induced_angina = models.FloatField(default=0)
    oldpeak = models.FloatField(default=0)
    slope = models.FloatField(default=0)
    no_of_major_vessel = models.FloatField(default=0)
    thalassemia = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True,null=True)



class Register(models.Model):
    username = models.CharField(max_length=20)
    email_address = models.EmailField()
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.username
