from django.urls import path
from . import views
from predict import views as p_views

urlpatterns = [
    path('', views.index, name='home'),
    path('hospital/', views.hospital, name='hospital'),
    path('doctor/', views.doctor, name='doctor'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<article_id>/', views.blog_detail, name="detail"),
    path('search/', p_views.search, name='search'),
    path('login', p_views.login_view, name='login'),
    path('logout/', p_views.logout_view, name='logout'),
    path('signup/', p_views.register_view, name='signup'),
]