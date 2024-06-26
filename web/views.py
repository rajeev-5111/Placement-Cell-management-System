from django.shortcuts import render,redirect
from .models import login_info,admin_info,student,company,feedback
# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        feedback(fname=fname,lname=lname,email=email,subject=subject,message=message).save()
        return render(request, 'contact.html',{'msg':'Details Submitted Successfully'})
    return render(request,'contact.html')

def apply(request):
    return render(request,'apply.html')


def student_registration(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        gender=request.POST['gender']
        dob=request.POST['dob']
        qualification=request.POST['qualification']
        city=request.POST['city']
        address=request.POST['address']
        resume=request.FILES['resume']
        student(name=name,email=email,phone=contact,gender=gender,qualification=qualification,dob=dob,city=city,address=address,resume=resume).save()
        return render(request,'student-registration.html',{'msg':'Registration Done Successfully'})
    return render(request,'student-registration.html')

def company_registration(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        city=request.POST['city']
        address=request.POST['address']
        company(name=name,email=email,phone=contact,city=city,address=address).save()
        return render(request,'company-registration.html',{'msg':'Details Successfully Submitted'})
    return render(request,'company-registration.html')

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if login_info.objects.filter(username=email,password=password).filter():
            data=login_info.objects.filter(username=email).get()
            if data.user_type=="admin":
                request.session['email']=email
                return redirect('adminn')
            return render(request,'admin/dashboard.html')
        return render(request,'login.html',{'msh':'Invalid Login Cridential'})
    return render(request,'login.html')

def adminn(request):
    if request.session['email']:
        email=request.session['email']
        data=admin_info.objects.filter(email=email).get()
        return render(request,'admin/dashboard.html',{'data':data})
    else:
        return redirect('login')

def view_feedback(request):
     if request.session['email']:
        email=request.session['email']
        data=admin_info.objects.filter(email=email).get()
        feed=feedback.objects.all()
        return render(request,'admin/view-feedback.html',{'data':data,'feed':feed})
     else:
        return redirect('signin')
     

def view_student(request):
     if request.session['email']:
        email=request.session['email']
        data=admin_info.objects.filter(email=email).get()
        data1=student.objects.all()
        return render(request,'admin/view-student.html',{'data':data,'data1':data1})
     else:
        return redirect('signin')

def view_company(request):
     if request.session['email']:
        email=request.session['email']
        data=admin_info.objects.filter(email=email).get()
        data1=company.objects.all()
        return render(request,'admin/view-company.html',{'data':data,'data1':data1})
     else:
        return redirect('signin')
     
def delete_company(request):
    if request.session['email']:
        email=request.GET['id']
        company.objects.filter(email=email).delete()
        return redirect('view-companies')
    else:
        return redirect('signin')
def delete_student(request):
    if request.session['email']:
        email=request.GET['id']
        student.objects.filter(email=email).delete()
        return redirect('view-students')
    else:
        return redirect('signin')
    
def logout(request):
    del request.session
    return redirect('signin')

def add_student(request):
     
     if request.session['email']:
        email=request.session['email']
        data=admin_info.objects.filter(email=email).get()
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            contact=request.POST['contact']
            gender=request.POST['gender']
            dob=request.POST['dob']
            qualification=request.POST['qualification']
            city=request.POST['city']
            address=request.POST['address']
            resume=request.FILES['resume']
            student(name=name,email=email,phone=contact,gender=gender,qualification=qualification,dob=dob,city=city,address=address,resume=resume).save()
            return render(request,'admin/add-student.html',{'msg':'Student Details Added','data':data})
        return render(request,'admin/add-student.html',{'data':data})
     else:
        return redirect('signin')

def add_company(request):
     
     if request.session['email']:
        email=request.session['email']
        data=admin_info.objects.filter(email=email).get()
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            contact=request.POST['contact']
            city=request.POST['city']
            address=request.POST['address']
            company(name=name,email=email,phone=contact,city=city,address=address).save()
            return render(request,'admin/add-company.html',{'msg':'Details Successfully Submitted','data':data})
        return render(request,'admin/add-company.html',{'data':data})
     else:
        return redirect('signin')