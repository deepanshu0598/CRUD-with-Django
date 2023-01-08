from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistration
from .models import User
# Create your views here.

# This function for adding or Showing recorde  
def add_show(request):
    if request.method == 'POST':
        fm=studentregistration(request.POST)
        if fm.is_valid():
            #fm.save()
            # or we can do this for any perticular data saving 
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pwd)
            reg.save()
            fm=studentregistration()
    else:
        fm=studentregistration()
    stu=User.objects.all()
    return render(request,'enroll/addAndShow.html',{'form':fm,"studata":stu})

#Function for Deleting recorde
def del_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#This function will update your data
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=studentregistration(instance=pi)
         
    return render(request,"enroll/updateStudent.html",{"form":fm})