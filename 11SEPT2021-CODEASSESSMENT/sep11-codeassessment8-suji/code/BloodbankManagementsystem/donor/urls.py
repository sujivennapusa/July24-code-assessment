from django.urls import path,include
from . import views
urlpatterns=[
    
    path('register/',views.register,name='register'),
    path('login/',views.logindonor,name='logindonor'),
   

    path('registerdonor/',views.donor_add,name='donor_add' ),
    
   
]