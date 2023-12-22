from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register_user/',views.register_user,name='register_user'),

    path('register_admin/',views.register_admin,name='register_admin'),

    path('register_seller/',views.register_seller,name='register_seller'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
]