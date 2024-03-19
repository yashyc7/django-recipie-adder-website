from django.shortcuts import redirect, render
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def recipie(request):
        
        data=Recipie.objects.all()
        if(request.method=='POST'):
            recipie_name=request.POST.get('recipie_name')
            recipie_description=request.POST.get('recipie_description')
            recipie_image=request.FILES.get('recipie_image')
            Recipie.objects.create(recipie_name=recipie_name,recipie_description=recipie_description,recipie_image=recipie_image)
        return render(request,"receipes.html",{'data':data})


def delete_recipie(request,id):
      data=Recipie.objects.get(id=id)
      data.delete()
      return redirect('/')
    
def update(request,id):
      queryset=Recipie.objects.get(id=id)
      if(request.method=='POST'):
            recipie_image=request.FILES.get('recipie_image')
            recipie_description=request.POST.get('recipie_description')
            recipie_name=request.POST.get('recipie_name')
            
            queryset.recipie_name=recipie_name
            queryset.recipie_description=recipie_description

            if recipie_image:
                  queryset.recipie_image=recipie_image

            queryset.save()
            return redirect('/')
      
      if request.GET.get('search'):
            queryset=queryset.filter(recipie_name__icontains=request.GET.get('search'))

      context={'recipie':queryset}
      return render(request,'update_recipies.html',context)



def login_page(request):
      if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            if not(User.objects.filter(username=username).exists()):
                  messages.error(request,'Invalid username')
                  return redirect('/login/') #user doesn't exist 
            #if user exists or not lets match the credentials of user from database using the authenticate function 
            user =authenticate(username=username,password=password)

            #if user credentials are not matched 
            if user is None:
                  messages.error(request,'Invalid password or username')
                  return redirect('/login/')
            else:
                  #user is logged in succesfully 
                  login(request,user)
                  return redirect('/')



      return render(request,'login.html')

def register(request):
      if request.method=='POST':
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=User.objects.filter(username=username)
            if user.exists():
                messages.info(request,'Username already taken ')
                return redirect('/register/')
            
            user=User.objects.create(
             first_name=first_name,
             last_name=last_name,
             username=username,
            )
            user.set_password(password)
            user.save()
            messages.info(request,'Account created succesfully')
            return redirect('/register/')

      return render(request,'register.html')


def logout_page(request):
      messages.info(request,'Account has been logged out ! ')
      logout(request)
      return redirect('/login/')