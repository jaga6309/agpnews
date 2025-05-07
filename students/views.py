from django.shortcuts import render
from students.forms import StudentForm

def create_student_view(request):
    if request.method=="POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        else:
            return render(request, "students/create_student.html", {"form": student_form})
    student_form = StudentForm()
    return render(request, "students/create_student.html", {"form": student_form})