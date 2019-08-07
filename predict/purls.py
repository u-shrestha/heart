from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register_view, name='signup'),
    path('predict/', views.index, name='predict'),
    path('myhistory/', views.history, name='history'),
    path('prediction/<id>/', views.history_detail, name='history_detail')

]