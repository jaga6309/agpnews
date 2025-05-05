from django.urls import path
from users.views import user_register_view

urlpatterns = [
    path("register/", user_register_view)
]
