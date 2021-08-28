from django.urls import path
from . import views
urlpatterns = [
path('addbook/',views.addbook,name='addbook'),
path('viewbook/',views.viewbook,name='viewallbook'),
path('viewbookdetails/<id>',views.viewbookdetails,name='viewdetails'),
path('searchapi/',views.searchapi,name='searchapi'),
path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
path('update_action_api/',views.update_data_read,name='update_data_read'),
path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
path('delete_action_api/',views.delete_data_read,name='delete_data_read'),


path('register/',views.register,name='registerbook'),
path('viewBooks/',views.bookview,name='bookview'),
path('searchBooks/',views.searchbook,name='searchbook'),
path('updateBooks/',views.update,name='updatebook'),
path('deleteBooks/',views.delete,name='deletehtml'),

]