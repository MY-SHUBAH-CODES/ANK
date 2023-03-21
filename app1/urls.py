
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home,name="home"),
    # path('blog/',views.blog,name="blog"),
    # path('contact/',views.contact,name="contact"),
    # path('services/',views.services,name="services"),
    # path('products/',views.products,name="products"),
    # path('featuredproducts/',views.featuredproducts,name="featuredproducts"),

    
    path('general_inquery/',views.general_inquery,name="general_inquery"),



    
]