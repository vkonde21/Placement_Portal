from django.urls import path
from placementportal import settings
from django.conf.urls.static import static
from .views import viewstudentprofile, verifystudent, verify,status, showfeedback, feedback, selectlist, deletecompany, results, withdraw, viewplacements, basic, register, profile, logout1, homepage, academicdetails, addcompany, viewcompany, viewdetails, apply, addskills, addshortlist, viewstudents
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', basic, name="basic"),
    path('home', homepage, name="homepage"),
    path('register/', register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name="login"),
    path('logout/', logout1, name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='portal/password_reset.html'), name="reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='portal/password_reset_done.html'), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='portal/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='portal/password_reset_complete.html'), name="password_reset_complete"),
    path('profile/', profile, name='profile'),
    path('academicinfo', academicdetails, name='academicdetails'), 
    path('add_company/', addcompany, name = 'addcompany'),
    path('viewcompany/',viewcompany, name = 'viewcompany' ), 
    path('viewdetails/<int:id>/', viewdetails, name = 'viewdetails'),
    path('apply/<int:id>/', apply, name='apply'), 
    path('addskills/', addskills, name='addskills'),
    path('addshortlist/<int:id>', addshortlist, name='addshortlist'),
    path('selectlist/<int:id>', selectlist, name='selectlist'),
    path('delete/<int:id>', deletecompany, name='deletecompany'),
    path('viewstudents/', viewstudents, name='viewstudents'),
    path('results/<int:c_id>', results, name='results'),
    path('withdraw/<int:c_id>', withdraw, name = 'withdraw'),
    path('viewplacements/', viewplacements, name = 'viewplacements'),
    path('feedback/', feedback, name="feedback"),
    path('showfeedback/', showfeedback, name = "showfeedback"),
    path('status/', status, name="status"),
    path('verify/',verify, name="verify"),
    path('verifystudent/<int:s_id>', verifystudent, name = "verifystudent"),
    path('viewprofile/<int:s_id>', viewstudentprofile, name='viewstudent')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
