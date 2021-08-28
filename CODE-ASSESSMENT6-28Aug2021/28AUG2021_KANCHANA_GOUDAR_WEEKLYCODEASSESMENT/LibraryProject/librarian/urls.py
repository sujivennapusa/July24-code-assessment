from django.urls import path,include
from . import  views

urlpatterns = [
    path('add/',views.Addlibrarian,name='Addlibrarian'),
    path('views/',views.Viewalllibrarian,name='Viewalllibrarian'),
    path('search/',views.Searchlibrarian,name='Searchlibrarian'),
    path('update/',views.Updatelibrarian,name='Updatelibrarian'),
    path('delete/',views.Deletelibrarian,name='Deletelibrarian'),

    path('addapi/',views.Librarianadd,name='Librarianadd'),
    path('viewallapi/',views.Librarianviewall,name='Librarianviewall'),
    path('viewapi/<fetchid>',views.Librarianview,name='Librarianview'),
    path('searchapi/',views.searchapi,name='searchapi'),
    path('update_searchapi/',views.update_searchapi,name='update_searchapi'),
    path('update_data/',views.update_data_read,name='update_data_read'),
    path('delete_searchapi/',views.delete_searchapi,name='delete_searchapi'),
    path('delete_data/',views.delete_data_read,name='delete_data_read'),
    
]
