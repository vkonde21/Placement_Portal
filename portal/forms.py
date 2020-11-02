from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Personaldetails, Student, Skills, Academics, Company, Criteria


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['resume', 'curr_year', 'curr_sem', 'b_id']
        labels = {'curr_year':'Current Year', 'curr_sem':'Current Semester', 'b_id':'Branch'}

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = Personaldetails
        fields = ['gender', 'dob', 'category', 'photo', 'address', 'phone']
        labels = {'dob': 'Date of Birth'}

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill_name', 'rating']
    
class AcademicsForm(forms.ModelForm):
    class Meta:
        model = Academics
        fields = ['semester', 'cgpa']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['c_name', 'address', 'contact', 'ctc', 'doa', 'recruitment_details', 'logo']
        labels = {'c_name':'Company Name', 'doa':'Date of Arrival', 'recruitment details':'Recruitment Details'}


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['c_name', 'address', 'contact',
                  'ctc', 'doa', 'recruitment_details', 'logo']


