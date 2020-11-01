from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from PIL import Image
import datetime

# Create your models here.


class Branch(models.Model):
    b_id = models.AutoField(primary_key = True)
    b_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.b_name

class Student(models.Model):
    choicesy = ((1, 'FY'), (2, 'SY'), (3, 'TY'), (4, 'Btech'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    s_id = models.IntegerField(primary_key=True)
    resume = models.FileField(upload_to='uploads/',validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])
    b_id = models.ForeignKey(Branch, null = True, on_delete=models.SET_NULL)
    curr_year = models.IntegerField(choices = choicesy, default = 1)
    curr_sem = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)], default = 1)
    status = models.BooleanField(default=False) #False means not placed
    verify = models.BooleanField(default = False) #False means details not verified

    

class Skills(models.Model):
    RATING_CHOICES = ((0, '0'),
                      (1, '1'),
                      (2, '2'),
                      (3, '3'),
                      (4, '4'),
                      (5, '5'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=150, unique=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    
class Personaldetails(models.Model):
    CHOICES = ((1, 'Male'),
                      (2, 'Female'),
                      (3, 'Other'))
    catchoice = ((1, 'OPEN'), (2, 'OBC'), (3, 'SC'), (4, 'ST'), (5, 'VJNT'))

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=CHOICES, default = 1)
    dob = models.DateField(default=datetime.date.today)
    category = models.IntegerField(choices = catchoice, default = 1)
    photo = models.ImageField(default='default.png', upload_to='photos/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    address = models.TextField(max_length = 300, default='', help_text='Please enter your address')
    phone = models.CharField(max_length = 10, validators = [MinLengthValidator(10), MaxLengthValidator(10)], default='0000000000')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if(img.height > 300 or img.width > 300):
            output = (300, 300)
            img.thumbnail(output)
            img.save(self.photo.path)

class Academics(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.IntegerField(models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]))
    cgpa = models.FloatField()



class Company(models.Model):
    c_id = models.AutoField(primary_key = True)
    c_name = models.CharField(max_length=150, unique=True)
    address = models.TextField(
        max_length=300, default='', help_text='Please enter your address')
    contact = models.CharField(max_length=10, validators=[MinLengthValidator(
        10), MaxLengthValidator(10)], default='0000000000')
    ctc = models.DecimalField(max_digits=10, decimal_places=2)
    doa = models.DateField(default=datetime.date.today) #date of arrival
    recruitment_details = models.TextField(
        max_length=1000, default='', help_text='Enter recruitment details')
    logo = models.ImageField(default='default.png', upload_to='company_logos/', validators=[
                             FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if(img.height > 300 or img.width > 300):
            output = (300, 300)
            img.thumbnail(output)
            img.save(self.logo.path)
    
class Shortlisted(models.Model):
    r_id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    round_name = models.CharField(max_length = 2000)


class Application(models.Model):
    Schoices = ((1, 'eligible'), (2, 'not eligible'), (3, 'selected'), (4, 'not selected'), (5, 'applied'), (6, 'not applied'))
    student = models.ForeignKey(Student,  on_delete=models.CASCADE)
    company = models.ForeignKey(Company,  on_delete=models.CASCADE)
    status = models.IntegerField(choices =Schoices, default = 6)
    class Meta:
        unique_together = (("company", "student", ),)

class Criteria(models.Model):
    SEM_CHOICES = ((1,1), (2, 2), (3, 3), (4, 4), (5, 5), (6,6), (7, 7), (8,8))
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    cgpa = models.FloatField(default=0.0)
    sem = models.IntegerField(choices=SEM_CHOICES,default=5)
    class Meta:
        unique_together = (("company", "branch", "sem"),)

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    post = models.TextField(max_length=2000, default='', help_text='Enter the post')




