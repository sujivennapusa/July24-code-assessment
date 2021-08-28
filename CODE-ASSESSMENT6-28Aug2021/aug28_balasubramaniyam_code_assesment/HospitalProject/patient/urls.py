from django.urls import path, include
from . import views

urlpatterns = [
    path('patient/',views.myPatient,name='myPatient'),
    path('',views.myWelcomePage,name='myWelcomePage'),
    path('viewallpatient/',views.myViewAllPage,name='myViewAllPage'),
    path('searchpatient/',views.mySearch,name='mySearch'),
    path('update/',views.myUpdate,name='myUpdate'),
    path('delete/',views.myDelete,name='myDelete'),

    path('deletesearch/',views.DeleteSearchAPI,name='DeleteSearchAPI'),
    path('deleteread/',views.DeleteRead,name='DeleteRead'),
    path('updateread/',views.UpdateRead,name='UpdateRead'),
    path('updatesearch/',views.UpdateSearchAPI,name='UpdateSearchAPI'),
    path('add/',views.myPatientPage,name='myPatientPage'),
    path('viewall/',views.myPatientList,name='myPatientList'),
    path('viewpatient/<id>',views.myPatientDetails,name='myCPatientDetails'),
    path('search/',views.SearchAPI,name='SearchAPI'),
]
