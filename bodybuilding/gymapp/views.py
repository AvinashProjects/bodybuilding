from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from gymapp.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    plan1 = Plan.objects.all()
    if request.method=='POST':
        n = request.POST['name']
        ph = request.POST['phone']
        pl = request.POST['plan']
        e = request.POST['email']
        m = request.POST['message']
        plan2 = Plan.objects.filter(name=pl).first()
        Member.objects.create(name=n, phone=ph, plan=plan2,email= e ,message=m)
        return redirect('home')
    d={'plan':plan1}
    return render(request,'gymapp/index.html',d)

def about(request):
    return render(request,'gymapp/about.html')

def services(request):
    return render(request,'gymapp/services.html')

def schedule(request):
    return render(request,'gymapp/schedule.html')

def gallery(request):
    return render(request,'gymapp/gallery.html')

def contact(request):
    return render(request,'gymapp/contact.html')

def blog(request):
    return render(request,'gymapp/blog.html')

def blogdetail(request):
    return render(request,'gymapp/blogdetails.html')

@csrf_exempt
def form(request):
    plan1 = Plan.objects.all()
    if request.method == 'POST':
        n = request.POST['name']
        ph = request.POST['phone']
        pl = request.POST['plan']
        e = request.POST['email']
        m = request.POST['message']
        plan2 = Plan.objects.filter(name=pl).first()
        Member.objects.create(name=n, phone=ph, plan=plan2, email=e, message=m)
        return redirect('home')
    d = {'plan': plan1}
    return render(request,'gymapp/form.html',d)

def elements(request):
    return render(request,'gymapp/element.html')

@csrf_exempt
def login_admin(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
        except:
            error = 'yes'

    d = {'error': error}
    return render(request, 'gymapp/login.html', d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('home')

    logout(request)
    return  redirect('home')

def view_members(request):
    mem=Member.objects.all()
    return render(request,'gymapp/view_members.html',{'members':mem})


