from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addlibrarian,name='addlibrarian'),
    path('viewall/',views.librarian_all,name='librarian_all'),
    path('view/<fetchid>',views.librarian_single,name='librarian_single'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('update/',views.librarianupdate,name='librarianupdate'),
    path('delete/',views.librariandelete,name='librariandelete'),


    path('register/',views.registerlibrarian,name='registerlibrarian'),
    path('vie/',views.librarianviewss,name='librarianviewss'),
    path('si/',views.librariansearch,name='librariansearch'),
    
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),

]