from django.contrib import admin
from .models import Article, Hospital, Doctor

# Register your models here.

admin.site.register(Article)
admin.site.register(Doctor)
admin.site.register(Hospital)