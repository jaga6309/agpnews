from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from users.models import Profile

def user_register_view(request):
    if request.method=="POST":
        data = request.POST
        usern = data.get("uname")
        em = data.get("eml")
        mob = data.get("mbl")
        firstn = data.get("fn")
        lastn = data.get("ln")
        pic=request.FILES.get("pro_pic")
        pswd = data.get("psw")
        cpassword = data.get("cpsw")
        if pswd!=cpassword:
            messages.warning(request, "Password and confirm password not matching.")
            return redirect("/users/register/")
        if User.objects.filter(username=usern).exists():
            messages.warning(request, "The username you given is already taken")
            return redirect("/users/register/")
        usr = User.objects.create_user(username=usern, email=em, first_name=firstn, last_name=lastn, password=pswd)
        # Profile.objects.create(mobile=mob, user=usr, profile_pic=pic)
        messages.success(request, "Your account ah been created successfully.")
    return render(request, "users/user_register.html")  

def user_login_view(request):
    if request.method=="POST":
        data = request.POST
        usern = data.get("uname")
        pswd = data.get("psw")
        user = authenticate(request, username=usern, password=pswd)
        if user is not None:
            login(request, user)
    return render(request, "users/user_login.html")

def user_logout_view(request):
    logout(request)
    return redirect("/users/login/")