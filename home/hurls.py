from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hospital/', views.hospital, name='hospital'),
    path('doctor/', views.doctor, name='doctor'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<article_id>/', views.blog_detail, name="detail")
]