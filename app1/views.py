from django.shortcuts import render
from .models import General_contact

def home(request):
    return render(request,"index.html")

# def about(request):
#     return render(request,"about.html")

# def contact(request):
#     return render(request,"contact.html")

# def services(request):
#     return render(request,"services.html")








def general_inquery(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        number=request.POST['Number']
        subject=request.POST['Subject']
        message=request.POST['Message']
        dat=General_contact.objects.create(name=name,email=email,number=number,subject=subject,message=message)
    return render(request,'index.html')

# def blog(request):
#     return render(request,'blog.html')




