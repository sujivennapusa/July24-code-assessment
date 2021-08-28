from django.urls import path,include
from . import views
urlpatterns=[
    
    path('add/',views.faculty_add,name='faculty_add'),
    path('viewall/',views.faculty_list,name='faculty_list'),
    path('view/<fetchid>',views.faculty_details,name='faculty_details'),

    path('register/',views.faculty_interface,name='faculty_interface'),
    path('viewfaculty/',views.view_list,name='view_list'),
    path('update/',views.update_list,name='update_list'),
    path('delete/',views.delete_list,name='delete_list'),
    path('search/',views.searchapi,name='searchapi'),
    path('searchview/',views.search_list,name='search_list'),
    path('updateapi/',views.updateapi,name='updateapi'),
    path('updateread/',views.update_read,name='update_read'),
    path('deleteapi/',views.deleteapi,name='deleteapi'),
    path('deleteread/',views.delete_read,name='delete_read'),
]