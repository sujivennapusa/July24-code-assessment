from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.booksPage,name="booksPage"),
    path('viewall/',views.books_list,name="books_list"),
    path('view/<fetchid>',views.books_details,name="books_details"),
    path('search/',views.searchapi,name='searchapi'),

    #html
    path('register/',views.register,name='register'),
    path('booksview/',views.viewall,name='viewall'),
    path('home/',views.home_view,name='home_view'),
    path('searchview/',views.search_view,name='search_view'),
    path('updatedata/',views.update_data_read,name='update_data_read'),
    path('updateapi/',views.update_api,name='update_api'),
    path('update/',views.update_view,name='update_view'),
    path('delete_api/',views.delete_api,name='delete_api'),
    path('deletedata/',views.delete_data_read,name='delete_data_read'),
    path('delete/',views.delete_view,name='delete_view'),
]
