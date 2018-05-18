from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-copyZ0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def login(self,request):
        if len(request.POST['email'])<2 and len(request.POST['password'])<2:
            messages.add_message(request,messages.ERROR,"please enter username and password")
            return False


        print("trying password......")
        user=User.objects.get(email=request.POST['email'])
        if(user.email==request.POST['email']):
            print("User match")
        print('checking password')
        if user.password==request.POST['password']:
            print("password match")
            return True
        else:
            messages.add_message(request,messages.ERROR,"User Doesn't Exist")
            return False
    def register(self,request):
        if len(request.POST['first_name'])<2:
            messages.add_message(request,messages.ERROR,"First Name can't be less than 2 letters")
            print("name Error")

        if len(request.POST['last_name'])<2:
            messages.add_message(request,messages.ERROR,"Last Name can't be less than 2 letters")
            print("desc Error")

        if not EMAIL_REGEX.match(request.POST['email']):
            messages.add_message(request,messages.ERROR,"please use valid Email address")

        if  User.objects.filter(email=request.POST['email']).count() >0:
            messages.add_message(request,messages.ERROR,"Email already registerd")
 

        if len(request.POST['password'])<8:
            messages.add_message(request,messages.ERROR,"Password can't be less than 8 letters")
            print("password Error")
        
        
        
        if(request.POST['password']!=request.POST['confirm_password']):
            messages.add_message(request,messages.ERROR,"Password do not match")


        if len(get_messages(request))>0:
            return False

        else:
            print("creating object")
            User.objects.create(first_name=request.POST['first_name'] ,last_name=request.POST['last_name'] , email=request.POST['email'] , password=request.POST['password'])
            print(User.objects.all())
            return True
            
             


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects=UserManager()
