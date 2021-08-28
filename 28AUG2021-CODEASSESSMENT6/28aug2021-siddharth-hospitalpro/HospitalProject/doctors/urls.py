from django.urls import path
from . import views
urlpatterns = [

path('adddoctor/',views.addDoctor,name='addDoctor'),
path('viewdoctors/',views.viewDoctor,name='viewallDoctor'),
path('viewdoctordetails/<id>',views.viewDoctordetails,name='viewdetails'),
path('searchapi/',views.searchapi,name='searchemp'),


path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
path('update_action_api/',views.update_data_read,name='update_data_read'),

path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
path('delete_action_api/',views.delete_data_read,name='delete_data_read'),








path('registeration/',views.register,name='Register'),
path('viewdoctor/',views.Doctorview,name='viewdoctorhtml'),
path('searchdoctor/',views.searchdoctor,name='searchhtml'),
path('updatedoctor/',views.update,name='updatehtml'),
path('deletedoctor/',views.delete,name='deletehtml'),
]