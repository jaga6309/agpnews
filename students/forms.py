from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    # extra_field = forms.CharField(max_length=10, required=True)
    class Meta:
        model = Student
        # fields = "__all__"
        # exclude = ["name", "roll_no"]
        # fields = ["name", "roll_no", "mobile", "extra_field"]
        fields = ["name", "roll_no", "mobile"]
    
    def clean_mobile(self):
        print(self.cleaned_data)
        mobile = self.cleaned_data.get("mobile")
        if len(mobile)<10:
            raise forms.ValidationError("Mobile number should be exactly 10 digits")
        return mobile