from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addfaculty,name='addfaculty'),
    path('viewall/',views.faculty_all,name='faculty_all'),
    path('view/<fetchid>',views.faculty_single,name='faculty_single'),



    
    path('search/',views.searchapi,name='searchapi'),
    path('register/',views.facultyregister,name='facultyregister'),
    path('viewfac/',views.facultyviewss,name='facultyviewss'),
    path('update/',views.facultyupdate,name='facultyupdate'),
    path('delete/',views.facultydelete,name='facultydelete'),
    path('search1/',views.facsearch,name='facsearch'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
    
    
]