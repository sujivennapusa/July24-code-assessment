from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.addFaculty,name='addFaculty'),
    path('viewall/',views.listFaculty,name='listFaculty'),
    path('view/<id>',views.view,name='view'),



    path('',views.faculty),
    path('viewfaculty/',views.viewFaculty),
    path('searchfaculty/',views.searchFaculty),
    path('deletefaculty/',views.deleteFaculty),
    path('updatefaculty/',views.updateFaculty),
    path('search/',views.search_api),

    path('update/',views.update_search,name="update_search"),
    path('update_data/',views.update_data,name='update_data'),
    path('delete_data/',views.delete_data,name='delete_data'),
    path('delete/',views.delete_search,name="delete_search"),

    path('home/',views.home)
    
    
    
]