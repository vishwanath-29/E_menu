from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def login(request):
    if(request.method=='POST'):
        user=request.POST['username']
        passwd=request.POST['password']
        user=auth.authenticate(request,username=user,password=passwd)
        if(user is not None):
            auth.login(request,user)
            return render(request,"add_edit/add_edit.html")
        else:
            messages.error(request,"invalid Credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')



def register(request):
    if request.method=='POST':
        name=request.POST['name1']
        email=request.POST['email_ID']
        passwd=request.POST['password1']
        confirm_passwd=request.POST['password2']
        
        if passwd==confirm_passwd:
            if User.objects.filter(username=name).exists():
                
                messages.error(request,'Username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request,'Already registered with this Email ID')
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,email=email,password=passwd)
                user.save()
                print("User saved")
                return redirect('/')
                
        else:
            messages.error(request,'Password Not Matching...')
            return redirect('register')
        
        

    
        
    else:
        return render(request,'accounts/register.html')
    
    