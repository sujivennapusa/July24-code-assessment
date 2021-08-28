from django.urls import path,include
from . import views
urlpatterns = [
    #VIEWS_HTML
    path('sub/',views.add_student_view,name='add_student_view'),
    path('viewallstudent/',views.viewall_student_view,name='viewall_student_view'),
    path('searchview/',views.search_student_view,name='search_student_view'),
    path('viewupdate/',views.update_student_view,name='update_student_view'),
    path('viewdelete/',views.delete_student_view,name='delete_student_view'),

    #APIS
    path('add/',views.student_create,name='student_create'),
    path('viewall/',views.student_list,name='student_list'),
    path('view/<id>',views.student_details,name='student_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('updatesearch/',views.updateapi,name='updateapi'),
    path('deletesearch/',views.deleteapi,name='deleteapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
    
   
]