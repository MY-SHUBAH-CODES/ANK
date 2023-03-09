from django.db import models

class General_contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=274)
    message=models.TextField(max_length=2000)
    read_status=models.BooleanField(default=False)
 
