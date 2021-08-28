from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addstudent,name='addstudent'),
    path('viewall/',views.student_all,name='event_all'),
    path('view/<fetchid>',views.student_single,name='student_single'),


    path('register/',views.register,name='register'),
    path('viewstd/',views.studentviewss,name='studentviewss'),
    path('update/',views.studentupdate,name='sudentupdate'),
    path('delete/',views.studentdelete,name='studentdelete'),
    path('search/',views.stdsearch,name='stdtsearch'),
    path('search1/',views.searchapi,name='searchapi'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
    


]