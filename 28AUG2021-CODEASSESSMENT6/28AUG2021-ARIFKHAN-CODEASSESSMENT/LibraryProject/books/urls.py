from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addbook,name='addbook'),
    path('viewall/',views.book_all,name='book_all'),
    path('view/<fetchid>',views.book_single,name='book_single'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('update/',views.bookupdate,name='bookupdate'),
    path('delete/',views.bookdelete,name='bookdelete'),


    path('register/',views.registerbook,name='registerbook'),
    path('vie/',views.bookviewss,name='bookviewss'),
    path('si/',views.booksearch,name='booksearch'),
    
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
]
