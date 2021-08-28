from . import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('add/',views.faculty,name='student'),
    path('viewall/',views.faculty_list,name='student_list'),
    path('view/<id>',views.facultydetail,name='studentdetail'),
    path('searchh/',views.searchp,name='search'),
    path('updatee/',views.updatee,name='update'),
    path('apiupdatee/',views.apiupdatee,name='apiupdate'),
    path('deletee/',views.deletee,name='delete'),
    path('apideletee/',views.apideletee,name='apidelete'),


    
    path('',views.addpagee,name='addpage'),
    path('viewpage1/',views.viewpagee,name='viewpage'),
    path('searchpage1/',views.searchpagee,name='searchpage'),
    path('updatepage1/',views.updatepagee,name='updatepage'),
    path('deletepage1/',views.deletepagee,name='deletepage'),
    
    
]
