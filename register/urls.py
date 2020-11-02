from django.contrib import admin
from django.urls import path
from register import views
app_name='register'
urlpatterns = [
    path('',views.index,name="index"),
    path('Login',views.index,name="index"),
    path('register',views.register,name="register"),
    path('Home',views.home,name="home"),
]
