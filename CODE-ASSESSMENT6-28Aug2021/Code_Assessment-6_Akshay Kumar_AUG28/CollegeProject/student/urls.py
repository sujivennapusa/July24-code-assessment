from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.addStudent,name='addStudent'),
    path('viewall/',views.listStudent,name='listFaculty'),
    path('view/<id>',views.view,name='view'),



    path('',views.student),
    path('viewstudent/',views.viewStudent),
    path('searchstudent/',views.searchStudent),
    path('deletestudent/',views.deleteStudent),
    path('updatestudent/',views.updateStudent),
    path('search/',views.search_api),

    path('update/',views.update_search,name="update_search"),
    path('update_data/',views.update_data,name='update_data'),
    path('delete_data/',views.delete_data,name='delete_data'),
    path('delete/',views.delete_search,name="delete_search"),
    
]