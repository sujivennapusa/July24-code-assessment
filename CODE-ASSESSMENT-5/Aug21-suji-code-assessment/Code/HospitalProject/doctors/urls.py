from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.doctor_add,name='doctor_add'),
    path('viewall/',views.doctor_list,name='doctor_list'),
    path('view/<fetchid>',views.doctor_details,name='doctor_details'),
    path('dcode/<fetchdoctor_code>',views.doctor_search,name='doctor_search'),
    path('register/',views.register_interface,name='register_interface'),
    path('login/',views.login_interface,name='login_interface'),

]