from django.shortcuts import redirect, render
from .models import * 
from django.http import HttpResponse
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



