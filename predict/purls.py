from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('activate/(P<uidb64>[0-9A-Za-z_\\-]+)/(P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate, name='activate'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='prediction/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='prediction/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='prediction/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='prediction/password_reset_complete.html'), name='password_reset_complete'),

]