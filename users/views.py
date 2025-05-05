from django.shortcuts import render
from django.contrib.auth.models import User
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