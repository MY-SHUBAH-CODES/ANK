from django.contrib import admin
from app1.models import *
# Register your models here.
class General_contact_admin(admin.ModelAdmin):
    list_display=['id','name','email','read_status','message']
admin.site.register(General_contact,General_contact_admin)

