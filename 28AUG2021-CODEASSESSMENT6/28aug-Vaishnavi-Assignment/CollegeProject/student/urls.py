from . import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('add/',views.student,name='student'),
    path('viewall/',views.student_list,name='student_list'),
    path('view/<id>',views.studentdetail,name='studentdetail'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('apiupdate/',views.apiupdate,name='apiupdate'),
    path('delete/',views.delete,name='delete'),
    path('apidelete/',views.apidelete,name='apidelete'),


   
    path('',views.addpage,name='addpage'),
    path('viewpage/',views.viewpage,name='viewpage'),
    path('searchpage/',views.searchpage,name='searchpage'),
    path('updatepage/',views.updatepage,name='updatepage'),
    path('deletepage/',views.deletepage,name='deletepage'),


]
