from django.urls import path
from . import views

urlpatterns=[
    path('',views.AuthenticationAdmin.admin_login, name='admin-login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.AuthenticationAdmin.SignOut,name='LogOut'),
    path('myprofiles/',views.myprofile,name='myprofile'),
]