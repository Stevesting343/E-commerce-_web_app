from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register_user(request):
    if request.method == "POST":
        u_name = request.POST.get("name")
        u_pass1 = request.POST.get("pwds1")
        u_pass2 = request.POST.get("pwds2")
        u_email = request.POST.get("email")
        u_type= request.POST.get("type_user")

        print(u_name,u_pass1,u_pass2,u_email,u_email,u_type)

        user = User.objects.create_user(username=u_name,password=u_pass1,email=u_email)
        user.save()
        d = Extend_User_Db(user=user,type_user=u_type)
        d.save()
        
        return redirect('login')

    return render(request,'register_user.html')

def register_admin(request):
    return render(request,'register_admin.html')

def register_seller(request):
    return render(request,'register_seller.html')    
    
def home(request):
    return render(request,'home.html')



