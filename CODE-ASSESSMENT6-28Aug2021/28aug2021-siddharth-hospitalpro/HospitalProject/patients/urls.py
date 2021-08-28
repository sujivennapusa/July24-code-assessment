from django.urls import path
from . import views
urlpatterns = [

path('addpatient/',views.addPatient,name='addpatient'),
path('viewpatient/',views.viewPatient,name='viewallpatient'),
path('viewpatientdetails/<id>',views.viewPatientdetails,name='viewdetails'),
path('searchapi/',views.searchapi,name='searchapi'),


path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
path('update_action_api/',views.update_data_read,name='update_data_read'),

path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
path('delete_action_api/',views.delete_data_read,name='delete_data_read'),


path('register/',views.register,name='registerpatienthtml'),
path('viewpatients/',views.Patientview,name='patientviewhtml'),
path('searchpatients/',views.searchpatient,name='searchpatienthtml'),
path('updatepatients/',views.update,name='updatepatienthtml'),
path('deletepatients/',views.delete,name='deletehtmlhtml'),





]