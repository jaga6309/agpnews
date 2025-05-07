from django.shortcuts import render

def super_admin_dashboard_view(request):
    return render(request, "super_admin/index.html")