from django.urls import path

from  . import  views
urlpatterns = [
    path('', views.showloginpage,name='showloginpage'),
    path('forgotpassword', views.forgotpassword,name='forgotpassword'),
    path('verifyRegistrationId', views.verifyRegistrationId, name='verifyRegistrationId'),


   # path('register', views.register, name='register'),
   # path('login', views.login, name='login'),


]