from django.shortcuts import render, redirect

def super_admin_dashboard_view(request):
    return render(request, "dashboard/dashboard.html")

def super_admin_profile_view(request):
    return render(request, "dashboard/profile.html")

def super_admin_password_change_view(request):
    return render(request, "dashboard/users/password_change.html")

def super_admin_user_list_view(request):
    return render(request, "dashboard/users/user_list.html")

def super_admin_user_detail_view(request, pk):
    return render(request, "dashboard/users/user_detail.html")

def super_admin_user_create_view(request):
    return render(request, "dashboard/users/user_create.html")

def super_admin_user_update_view(request, pk):
    return render(request, "dashboard/users/user_update.html")

def super_admin_user_delete_view(request, pk):
    return redirect(".")

def super_admin_user_activate_view(request, pk):
    return redirect(".")

def super_admin_user_dactivate_view(request, pk):
    return redirect(".")

def super_admin_category_list_view(request):
    return render(request, "dashboard/news/category_list.html")

def super_admin_category_create_view(request):
    return render(request, "dashboard/news/category_create.html")

def super_admin_category_update_view(request, pk):
    return render(request, "dashboard/news/category_update.html")

def super_admin_category_detail_view(request, pk):
    return render(request, "dashboard/news/category_detail.html")

def super_admin_category_delete_view(request):
    return redirect(".")

def super_admin_tag_create_view(request):
    pass

def super_admin_tag_update_view(request, pk):
    pass

def super_admin_tag_delete_view(request, pk):
    pass

def super_admin_article_list_view(request):
    return render(request, "dashboard/news/article_list.html")

def super_admin_article_create_view(request):
    return render(request, "dashboard/news/article_create.html")

def super_admin_article_update_view(request, pk):
    pass

def super_admin_article_detail_view(request, pk):
    pass

def super_admin_article_delete_view(request, pk):
    pass

def super_admin_article_status_update_view(request, pk):
    pass

def super_admin_article_publish_view(request, pk):
    pass
    
def super_admin_article_unpublish_view(request, pk):
    pass
