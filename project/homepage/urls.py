from django.contrib import admin
from django.urls import path
from homepage import views

app_name='homepage' 
urlpatterns = [
    path('',views.postapic,name="postapic"),
    path('logout',views.logout,name="logout"),
    path('createpost',views.create,name="create"),
    path('profile',views.profile,name="create"),
]
