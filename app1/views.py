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

def products(request):
    return render(request,"products.html")

def featuredproducts(request):
    return render(request,"featuredproducts.html")






# def general_contact(request):
#     if request.method=='POST':
#         name=request.POST['Name']
#         email=request.POST['Email']
#         message=request.POST['Message']
#         dat=General_contact.objects.create(name=name,email=email,message=message)
#     return render(request,'index.html')




