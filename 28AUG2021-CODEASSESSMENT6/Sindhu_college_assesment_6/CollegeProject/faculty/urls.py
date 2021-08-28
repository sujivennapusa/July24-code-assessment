from django.urls import path,include
from . import views
urlpatterns = [
    #views
    path('reg/',views.add_faculty_view,name='add_faculty_view'),
    path('viewallfaculty/',views.viewall_faculty_view,name='viewall_faculty_view'),
    path('searchview/',views.search_faculty_view,name='search_faculty_view'),
    path('viewupdate/',views.update_faculty_view,name='update_faculty_view'),
    path('viewdelete/',views.delete_faculty_view,name='delete_faculty_view'),
   
    #view api
    path('add/',views.faculty_create,name='faculty_create'),
    path('viewall/',views.faculty_list,name='faculty_list'),
    path('view/<id>',views.faculty_details,name='faculty_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('updatesearch/',views.updateapi,name='updateapi'),
    path('deletesearch/',views.deleteapi,name='deleteapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
    
    
   
]