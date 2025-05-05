from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.models import Profile

def user_register_view(request):
    if request.method=="POST":
        data = request.POST
        usern = data.get("uname")
        em = data.get("eml")
        mob = data.get("mbl")
        firstn = data.get("fn")
        lastn = data.get("ln")
        pswd = data.get("psw")
        cpassword = data.get("cpsw")
        usr = User.objects.create_user(username=usern, email=em, first_name=firstn, last_name=lastn, password=pswd)
        Profile.objects.create(mobile=mob, user=usr)
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