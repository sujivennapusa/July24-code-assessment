from django.urls import path, include
from . import views

urlpatterns = [
    path('doctor/',views.myDoctor,name='myDoctor'),
    path('welcomedoctor/',views.myWelcomeDoctorPage,name='myWelcomeDoctorPage'),
    path('viewalldoctor1/',views.myViewAllPage1,name='myViewAllPage1'),
    path('searchdoctor/',views.mySearch1 ,name='mySearch1'),
    path('update1/',views.myUpdate1,name='myUpdate1'),
    path('delete1/',views.myDelete1,name='myDelete1'),
  

    path('deletesearch1/',views.DeleteSearchAPI1,name='DeleteSearchAPI1'),
    path('deleteread1/',views.DeleteRead1,name='DeleteRead1'),
    path('updateread1/',views.UpdateRead1,name='UpdateRead1'),
    path('updatesearch1/',views.UpdateSearchAPI1,name='UpdateSearchAPI1'),
    path('add/',views.myDoctorPage,name='myDoctorPage'),
    path('viewall1/',views.myDoctorList,name='myDoctorList'),
    path('viewdoctor1/<id>',views.myDoctorDetails,name='myDoctorDetails'),
    path('search1/',views.SearchAPI1,name='SearchAPI1'),
]
