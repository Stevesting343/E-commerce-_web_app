from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('inde/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logins/',views.logins,name='logins'),
    path('home/',views.home,name='home'),
    path('logouts/',views.logouts,name='logouts'),
    path('display_buyer/',views.display_buyer,name='display_buyer'),
    path('perinfo_buyur',views.perinfo_buyer,name='perinfo_buyer'),
]