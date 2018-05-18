from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

def index(request):
    

    return render(request,"lrApp/index.html")

def success(request,id):
    print("Got to success")

    return redirect('/register')

def register(request):
    print("in register")
    
    if User.objects.register(request):
        print("user created")
        user=User.objects.get(email=request.POST['email'])
        name=user.first_name+" "+user.last_name
        return render(request,"lrApp/success.html",{'user_name':name})
    else:
        return redirect('/')

def login(request):
    print("in login")
    if User.objects.login(request):
        print("logged in")
        user=User.objects.get(email=request.POST['email'])
        name=user.first_name+" "+user.last_name
        return render(request,"lrApp/success.html",{'user_name':name})
    else:
        return redirect('/')



def delete(request):
    if(User.objects.first()):
        while(User.objects.first()):
            User.objects.first().delete()
        messages.add_message(request,messages.ERROR,"All user deleted")
        return redirect("/")
    else:
        return redirect("/")