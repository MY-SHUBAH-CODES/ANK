from django.shortcuts import render,redirect
from .models import General_contact

def home(request):
    return render(request,"index.html")


def general_inquery(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        number=request.POST['Number']
        subject=request.POST['Subject']
        message=request.POST['Message']
        dat=General_contact.objects.create(name=name,email=email,number=number,subject=subject,message=message)
    return render(request,'index.html')


def search(request):
    if request.method=='POST':
        searchkey=request.POST['searchkey']
        print(searchkey)
    return redirect(request,'#')




