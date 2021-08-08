from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('',views.home,name="home"),
    path('pubg',views.pubg,name="pubg"),
    path('freefire',views.freefire,name="freefire"),
    path('pes',views.pes,name="pes"),
    path('pubg_join',views.pubg_join,name="pubg_join"),
    path('pubg_join_10_taka',views.pubg_join_10_taka,name="pubg_join_10_taka"),
    path('freefire_join',views.freefire_join,name="freefire_join"),
    path('account',views.account.as_view(),name="account"),
    path('register_form_pubg',views.register_form_pubg,name="register_form_pubg"),
    path('register_form_freefire',views.register_form_freefire,name="register_form_freefire"),
    path('register_form_pubg_10_taka',views.register_form_pubg_10_taka,name="register_form_pubg_10_taka"),
    path('signinn/',views.signinn,name="signinn"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('contact/',views.contact,name="contact"),
    
    
]