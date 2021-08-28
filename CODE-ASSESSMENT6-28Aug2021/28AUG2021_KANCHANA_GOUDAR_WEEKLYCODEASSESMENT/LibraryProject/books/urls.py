from django.urls import path,include
from . import views

urlpatterns = [

    path('add/',views.Addbook,name='Addbook'),
    path('views/',views.Viewallbook,name='Viewallbook'),
    path('search/',views.Searchbook,name='Searchbook'),
    path('update/',views.Updatebook,name='Updatebook'),
    path('delete/',views.Deletebook,name='Deletebook'),

    path('addapi/',views.Bookadd,name='Bookadd'),
    path('viewallapi/',views.Bookviewall,name='Bookviewall'),
    path('viewapi/<fetchid>',views.Bookview,name='Bookview'),
    path('searchapi/',views.searchapi,name='searchapi'),
    path('update_searchapi/',views.update_searchapi,name='update_searchapi'),
    path('update_data/',views.update_data_read,name='update_data_read'),
    path('delete_searchapi/',views.delete_searchapi,name='delete_searchapi'),
    path('delete_data/',views.delete_data_read,name='delete_data_read'),
]
