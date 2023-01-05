from django.shortcuts import render, redirect
from students.models import Account, Students
from admin.models import Department

# Create your views here.


def add_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        obj = Account(username = username, password = password, type = "admin")
        obj.save()

    return render(request,'add_admin.html')


def add_department(request):
    if request.method == "POST":
        dep = request.POST['dep']

        obj = Department(department = dep)
        obj.save()
    return render(request,'add_department.html')




def index_admin(request):
    return render(request,'index_admin.html')


def view_register(request):
    obj = Students.objects.all()
    return render(request,'view_register.html',{'students':obj})



def manage_department(request):
    obj = Department.objects.all()
    return render(request,'manage_department.html',{'departments':obj})



def update(request, idd):
    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']

        Students.objects.filter(id = idd).update(name = name, place = place, email = email, contact = contact)
        return redirect('admin:view_register')
    aa = Students.objects.get(id = idd)
    return render(request,'update.html',{'updates':aa})