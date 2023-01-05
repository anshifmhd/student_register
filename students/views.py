
from django.shortcuts import render, redirect
from students.models import Students,Account
from admin.models import Department

# Create your views here.



def register_students(request):
    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        department_id = request.POST['department']
        department = Department.objects.get(id = department_id)
        username = request.POST['username']
        password = request.POST['password']


        obj = Students( name=name, email=email, contact=contact, place=place, department=department)
        obj.save()
        account = Account( username = username, password = password, type = 'student', student_id = obj.id )
        account.save()
    return render(request,'register_students.html',{'departmnets': Department.objects.all()})



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Account.objects.get(username = username, password = password)
            request.session['userid'] = user.id
            if (user.type == 'student'):
                return redirect('after_login')
            elif(user.type == 'admin'):
                return redirect('admin:index_admin')
        except:
            return render(request, 'login.html',{'message':'username or password is incorrect'})

    return render(request,'login.html')



def index(request):
    return render(request,'index.html')


def after_login(request):
    
    return render(request,'after_login.html')