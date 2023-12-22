from django.shortcuts import render,redirect, HttpResponse,HttpResponseRedirect,reverse

from . models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def logins(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pass1 = request.POST.get('pwds1')
        user = authenticate(username=name,password=pass1)
        print("-------hiii",type(user))
        if user is not None:
            login(request,user)
            print("------------------")
            return redirect('home')
        else:
            return HttpResponse('user not present')
    return render(request,'login.html')

def register(request):
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
        return redirect('logins')
    return render(request,'register.html') 
    
def home(request):
    return render(request,'home.html')


def logouts(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('logins'))

     
def display_buyer(request):
    return render(request,'display_buyer.html')

def perinfo_buyer(request):
    return render(request,'personal_info_buyer.html')