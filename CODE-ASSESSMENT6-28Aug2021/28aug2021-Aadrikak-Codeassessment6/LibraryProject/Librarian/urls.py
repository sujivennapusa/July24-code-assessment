from django.urls import path
from . import views
urlpatterns = [
path('addLibrarian/',views.addLibrarian,name='addEmp'),
path('viewlibrarian/',views.viewLibrarian,name='viewallEmp'),
path('viewLibrariandetails/<id>',views.viewLibdetails,name='viewdetails'),
path('searchapi/',views.searchapi,name='searchemp'),


path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
path('update_action_api/',views.update_data_read,name='update_data_read'),
path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
path('delete_action_api/',views.delete_data_read,name='delete_data_read'),


path('register/',views.register,name='Register'),
path('viewLibrarian/',views.Librarianview,name='viewemphtml'),
path('searchLibrarian/',views.searchemp,name='searchhtml'),
path('updateLibrarian/',views.update,name='updatehtml'),
path('deleteLibrarian/',views.delete,name='deletehtml'),
]