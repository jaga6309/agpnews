from django.urls import path
from students.views import create_student_view

urlpatterns = [
    path("create/", create_student_view)
]
