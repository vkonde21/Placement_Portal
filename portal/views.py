from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, StudentUpdateForm, PersonalDetailsForm, SkillsForm, AcademicsForm, CompanyForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from .models import Student, Personaldetails, Academics, Branch, Criteria, Application, Company, Skills, Shortlisted, Feedback
import json
from datetime import date
# Create your views here.


def basic(request):
    return redirect("/home")

@login_required
def homepage(request):
    if(request.user.is_superuser == False):
        context = {}
        avg_cgpa = 0
        #calculate avg cgpa
        academic = Academics.objects.filter(student = request.user.student)
        avg_cgpa = academic.aggregate(Avg('cgpa'))['cgpa__avg']
        #for all companies visiting the campus check if student is eligible or not
        if(avg_cgpa != None):
            a = Application.objects.filter(student = request.user.student)
            context['companies'] = a
        else:
            msg = "Update academic and personal details to apply for companies!!"
            context['msg'] = msg

    else:
        context = {'a':1}
    return render(request, 'portal/homepage.html', context)
def register(request):
    form = UserRegisterForm()
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            messages.success(request, f"Account created for {username} !!")
            form.save()
            user = User.objects.get(username=username)
            profile = Student(user=user)
            profile.save()
            profile = Student.objects.get(user = user)
            prof = Personaldetails(student=profile)
            prof.save()
            return redirect("/login")

    return render(request, 'portal/register.html', {"form": form})




@login_required
def profile(request):
    if(request.user.is_superuser == False):
        if(request.method == "POST"):
            u_form = UserUpdateForm(
                request.POST, request.FILES, instance=request.user)
            p_form = StudentUpdateForm(
                request.POST, request.FILES, instance=request.user.student)
            d_form = PersonalDetailsForm(request.POST, instance=request.user.student.personaldetails)
            
            u_name = request.POST.get("username")
            print(u_name)
            print(request.user.username)
            if(u_form.is_valid() and p_form.is_valid() and d_form.is_valid()):
                #
                if(u_name != request.user.username):
                    p = User.objects.filter(u_name)
                    if(len(p) > 0):
                        messages.error(request, "Username already exists")
                        return redirect("/profile")
                u_form.save()
                p_form.save()
                d_form.save()
                messages.success(request, "Profile Updated!!")
                return redirect("/profile")

        else:
            u_form = UserUpdateForm(instance= request.user)
            p_form = StudentUpdateForm(instance= request.user.student)
            d_form = PersonalDetailsForm(instance=request.user.student.personaldetails)

        context = {"p_form": p_form, "u_form":u_form, "d_form":d_form, 's' : 1}
        return render(request, 'portal/profile.html',context)
    else:
        if(request.method == 'POST'):
            u_form = UserUpdateForm(
                request.POST, request.FILES, instance=request.user)
            u_name = request.POST.get("username")
            print(u_name)
            print(request.user.username)
            if(u_form.is_valid()):
                #
                if(u_name != request.user.username):
                    p = User.objects.filter(u_name)
                    if(len(p) > 0):
                        messages.error(request, "Username already exists")
                        return redirect("/profile")
                u_form.save()
                messages.success(request, "Profile Updated!!")
                return redirect("/profile")
        else:
            u_form = UserUpdateForm(instance=request.user)
            context = {"u_form": u_form,}
            return render(request, 'portal/profile.html', context)


@login_required
def academicdetails(request):
    if(request.method == "POST"):
        s = request.user.student
        for i in range(1, s.curr_sem):
            c = request.POST["sem"+str(i)]
            a = Academics(student = request.user.student, semester = i, cgpa = c)
            a.save()
            
        messages.success(request, f"Academic details saved successfully!!")
        return render(request, 'portal/skills.html', {'range':range(0, 6)})
    else:
        s = request.user.student
        a = Academics.objects.filter(student = s)
        f = ''
        d = {}
        for i in range(1, s.curr_sem):
            f = f + str(i)
            if(a):
                x = a.filter(semester = i)
                if(x):
                    d['sem' + str(i)] = x[0].cgpa
                else:
                    d['sem' + str(i)] = 0

        d['f'] = f
        return render(request, 'portal/academics.html', d)

@login_required
def addskills(request):
    if(request.method == 'POST'):
        a = request.POST.get('am')
        #try:
        for i in range(1, int(a) + 1):
            sname = request.POST.get("skill" + str(i))
            rating = request.POST.get("rating" + str(i))
            print(sname)
            print(rating)
            '''if(sname != None and rating != None):
                s = Skills(skill_name = sname, rating = rating, student = request.user.student)
                s.save()'''
        messages.success(request, 'Your skills have been saved!!!')
        #except:
            #messages.error(request,"An error occured!!")
        return redirect('/home')


def addcompany(request):
    if(request.method == "POST"):
        c_form = CompanyForm(request.POST, request.FILES)
        if(c_form.is_valid()):
            #check if the company is already present
            name = request.POST.get("c_name")
            company = c_form.save()
            a = request.POST.get("am")
            for i in range(1, int(a) + 1):
                n = request.POST.get("exampleFormControlSelect" + str(i))
                if(n != None):
                    cgpa = request.POST.get("sem" + str(i))
                    sem = request.POST.getlist('semselect' + str(i)) #getlist for multiple select values
                    print(n,cgpa, sem )
                    branch = Branch.objects.get(b_name = n)
                    for x in sem:
                        c = Criteria(branch = branch, cgpa = cgpa, sem = int(x), company = company)
                        c.save()
            messages.success(request, f"{name} company added successfully!!")
            #generate application forms for each student for this company
            s = Student.objects.all()
            for i in s:
                flag = 0
                if(i.status == False):
                    academic = Academics.objects.filter(
                        student=i)
                    avg_cgpa = academic.aggregate(Avg('cgpa'))['cgpa__avg']
                    #check if criteria is satisfied
                    criteria = Criteria.objects.filter(company=company)
                    for j in criteria:
                        print(j.cgpa, avg_cgpa)
                        print(i.curr_sem, j.sem)
                        
                        if(j.cgpa <= avg_cgpa and i.curr_sem == j.sem and i.b_id == j.branch):
                            a = Application(student = i, company = company, status = 1)
                            a.save()
                            flag = 1
                            break
                if(flag == 0):
                    a = Application(student=i, company=company, status=2)
                    a.save()
                
        else:
            messages.error(request, f"Failed to add company details!!")
        return redirect('/home')
    else:
        c_form = CompanyForm()
        branch = Branch.objects.all()
        return render(request, 'portal/addcompany.html', {'c_form':c_form, 'branch':branch,'range':range(1,9)})

def viewcompany(request):
    cs = Company.objects.all()
    return render(request, 'portal/viewcompanies.html', {'company':cs})

def viewdetails(request, id):
    try:
        cs = Company.objects.get(c_id = id)
        rounds = Shortlisted.objects.filter(company__c_id = id)
        roundnames = rounds.values_list(('round_name'), flat = True).distinct()
        r = {}
        print(roundnames)
        for i in roundnames:
            x = rounds.filter(round_name = i)
            r[i]  =  x

    except:
        messages.error(request, 'Company deleted from the records!!!')
        return redirect('/viewcompany')
    return render(request, 'portal/companydetails.html', {'company':cs, 'r':r})

def apply(request, id):
    c_id = id
    company = Company.objects.get(c_id = id)
    student = Student.objects.get(user = request.user)
    q = Application.objects.get(company__c_id = c_id, student = student)
    if(date.today() <= company.doa ):
        if(q.status == 1):
            q.status = 5
            q.save()
            messages.success(request, 'Applied for the company successfully!!')
        else:
            messages.success(
                request, 'You are not eligible!!')

    else:
        messages.error(request, 'Too late to apply!!')
    return redirect('/home')

def addshortlist(request, id):
    if(request.method == "POST"):
        pass
    else:
        return render(request, 'portal/shortlist.html', {'i':id})

def selectlist(request, id):
    if(request.method == "POST"):
        #print()
        c = Company.objects.get(c_id = id)
        round_name = request.POST.get('am')
        for x in request.POST.getlist('name'):
            s = Student.objects.get(s_id = int(x))
            sh = Shortlisted(company = c, student = s, round_name = round_name)
            sh.save()
        messages.success(request, 'Shortlist created successfully!!!')
        shrounds = Shortlisted.objects.filter(company__c_id = id)
        rounds = shrounds.values_list(('round_name'), flat = True).distinct()
        r = {}
        #print(rounds)
        for i in rounds:
            r[i] = shrounds.filter(round_name = i)
        #print(r)
        c_id = id
        return render(request, 'portal/allshortlist.html', {'r':r, 'c_id':c_id})
    else:
        round1 = request.GET.get("round1")
        apps = Application.objects.filter(company__c_id = id, status = 5)
        print(apps)
        return render(request, 'portal/studentlist.html', {'apps':apps, 'round1':round1, 'id':id, 'shortlist':1})
def results(request, c_id):
    #final shortlist
    if(request.method == "POST"):
        c = Company.objects.get(c_id=c_id)
        round_name = request.POST.get('am')
        for x in request.POST.getlist('name'):
            s = Student.objects.get(s_id=int(x))
            s.status = True
            s.save()
            a = Application.objects.get(company__c_id = c_id, student__s_id = int(x))
            a.status = 3
            a.save()
            sh = Shortlisted(company=c, student=s, round_name=round_name)
            sh.save()
        allapps = Application.objects.filter(company__c_id=c_id).values_list('student__s_id')
        for i in allapps:
            s = Application.objects.get(student__s_id = i[0], company__c_id = c_id)
            if(s.status != 3 and s.status != 1 and s.status != 2):
                s.status = 4
                s.save()
            elif(s.status == 1):
                s.status = 6
                s.save()
            
        messages.success(request, "Results updated!!")
        return redirect('/home')

    else:
        apps = Application.objects.filter(company__c_id=c_id, status=5)
        round1 = 'Final Shortlist'
        print("In results", apps)
        return render(request, 'portal/studentlist.html', {'apps': apps, 'round1': round1, 'id': c_id, 'final': 1})

def withdraw(request, c_id):
    d = date.today()
    c = Company.objects.get(c_id = c_id)
    if(c.doa >= d):
        a = Application.objects.get(student = request.user.student, company = c)
        a.status = 1
        a.save()
        messages.success(request, 'Your application has been withdrawn!!')
    else:
        messages.error(request, 'Your application cannot be withdrawn!!')
    return redirect('/home')

def viewplacements(request):
    apps = Application.objects.filter(status = 3)
    return render(request, 'portal/viewplacements.html', {'apps':apps})

def feedback(request):
    #try:
    if(request.method == 'POST'):
        s_id = int(request.POST.get("sid"))
        c_id = int(request.POST.get('cid'))
        post = request.POST.get('post')
        student = Student.objects.get(s_id = s_id)
        company = Company.objects.get(c_id = c_id)
        g = Feedback.objects.filter(student = student, company  = company)
        if(len(g) > 0):
            g = Feedback.objects.get(student=student, company=company)
            g.delete()
        f = Feedback(student = student, company = company, post = post)
        f.save()
        messages.success(request, 'Feedback saved')
        #except:
            #messages.error(request, 'Could not be saved')
        return redirect('/home')
    else:
        return render(request, 'portal/feedback.html')
def showfeedback(request):
    f = Feedback.objects.filter(student = request.user.student)
    return render(request, 'portal/showfeedback.html', {'f':f})
    

def status(request):
    #perfomance uptill now
    st= request.user.student
    i = st.s_id
    s = Shortlisted.objects.filter(student = request.user.student)
    d = {}
    for i in s:
        try:
            d[i.company].append(i)
        except:
            d[i.company] = [i]
    return render(request, 'portal/status.html',{'r':d})

def verify(request):
    s = Student.objects.filter(verify = False)
    return render(request, 'portal/verify.html', {'s':s})

def verifystudent(request, s_id):
    if(request.method == "GET"):
        s = Student.objects.get(s_id=s_id)
        skills = Skills.objects.filter(student=s)
        academics = Academics.objects.filter(student=s)
        return render(request, 'portal/viewprofile.html', {'student': s, 'skills': skills, 'academics': academics, 'verify':1})
    s = Student.objects.get(s_id = s_id)
    s.verify = True
    s.save()
    messages.success(request, "Student details verified!!")
    return redirect('/verify')
        
def viewstudentprofile(request, s_id):
    s = Student.objects.get(s_id = s_id)
    skills = Skills.objects.filter(student = s)
    academics = Academics.objects.filter(student = s)
    return render(request, 'portal/viewprofile.html', {'student':s, 'skills':skills, 'academics':academics})

def deletecompany(request, id):
    c = Company.objects.get(c_id = id)
    c.delete()
    messages.success(request, 'Deleted the company details successfully!!!')
    return redirect('/viewcompany')

def viewstudents(request):
    s = Student.objects.all()
    return render(request, 'portal/studentlist.html', {'student':s})
    
def logout1(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/home")
