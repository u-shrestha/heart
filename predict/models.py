from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Heart(models.Model):
    name =models.ForeignKey(User, related_name='Heart.name+', on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    sex = models.IntegerField()
    chest_pain_type = models.FloatField()
    resting_bloodpressure = models.FloatField()
    serum_cholestrol = models.FloatField()
    fasting_blood_sugar = models.FloatField()
    resting_ecg = models.FloatField()
    max_heartrate = models.FloatField()
    exercise_induced_angina = models.FloatField()
    oldpeak = models.FloatField()
    slope = models.FloatField()
    no_of_major_vessel = models.FloatField()
    thalassemia = models.FloatField()
    created = models.DateTimeField(auto_now_add=True,null=True)
