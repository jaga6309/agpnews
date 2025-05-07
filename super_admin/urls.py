from django.urls import path
from super_admin.views import super_admin_dashboard_view

urlpatterns = [
    path("dashboard/", super_admin_dashboard_view)
]
