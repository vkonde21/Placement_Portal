from django.contrib import admin
from .models import Academics, Branch, Personaldetails, Skills, Student, Company, Criteria, Application, Shortlisted, Feedback

admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Skills)
admin.site.register(Personaldetails)
admin.site.register(Academics)
admin.site.register(Company)
admin.site.register(Criteria)
admin.site.register(Application)
admin.site.register(Shortlisted)
admin.site.register(Feedback)


