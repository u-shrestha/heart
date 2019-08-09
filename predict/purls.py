from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register_view, name='signup'),
    path('myaccount/changepassword/', views.change_password, name='changepassword'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('predict/', views.index, name='predict'),
    path('myhistory/', views.history, name='history'),
    path('myhistory/<id>/', views.history_detail, name='history_detail'),
    path('user/', views.user, name='user'),
]