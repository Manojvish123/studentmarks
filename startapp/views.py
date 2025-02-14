from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("hello gyan sagar")

def loginpage(request):
    return HttpResponse("welcome in login page")
    
def logoutpage(request):
    return HttpResponse("thank you you are log out")

from .models  import Studentmarks
def marks(request):
    if request.method=="POST":
        sub1= request.POST.get('sub1')
        sub2= request.POST.get('sub2')
        sub3= request.POST.get('sub3')
        sub4= request.POST.get('sub4')
        sub5= request.POST.get('sub5')
        temp=Studentmarks(Sub1=sub1,Sub2=sub2,Sub3=sub3,Sub4=sub4,Sub5=sub5)
        temp.save()
    return render(request,"marks.html")

