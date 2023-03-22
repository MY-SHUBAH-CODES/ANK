
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home,name="home"),
    path('general_inquery/',views.general_inquery,name="general_inquery"),
    
    # path('search/',views.search,name="search"),
    path('search/',views.search,name="search"),

    
    


    
]