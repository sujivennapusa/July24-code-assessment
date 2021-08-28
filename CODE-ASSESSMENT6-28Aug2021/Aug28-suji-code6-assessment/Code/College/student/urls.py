from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.student_add,name='student_add'),
    path('viewall/',views.student_list,name='student_list'),
    path('view/<fetchid>',views.student_details,name='student_details'),
    
    
    path('register/',views.student_interface,name='student_interface'),
    path('viewstudent/',views.view_list,name='view_list'),
    path('update/',views.update_list,name='update_list'),
    path('delete/',views.delete_list,name='delete_list'),
    path('searchview/',views.search_list,name='search_list'),
    path('search/',views.searchapi,name='searchapi'),
    path('updateapi/',views.updateapi,name='updateapi'),
    path('updateread/',views.update_read,name='update_read'),
    path('deleteapi/',views.deleteapi,name='deleteapi'),
    path('deleteread/',views.delete_read,name='delete_read'),
]