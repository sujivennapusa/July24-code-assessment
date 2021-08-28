from django.urls import path,include
from . import views

urlpatterns = [


    path('sadd/',views.studentaddpage,name='studentaddpage'),
    path('viewall/',views.student_list,name='student_list'),
    path('viewstudents/<fetchid>',views.student_details,name='student_details'),
    path('add/',views.student_view,name='student_view'),
    path('viewstudent/',views.stu_view,name='stu_view'),
    path('searchstudent/',views.search_view,name='search_view'),
    path('deletestudent/',views.delete_view,name='delete_view'),
    path('updatestudent/',views.update_view,name='update_view'),
    path('search/',views.searchapi,name='searchapi'),
    path('updateactionapi/',views.update_data_read,name='update_data_read'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteactionapi/',views.delete_data_read,name='delete_data_read'),




]