from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.patient_add,name='patient_add'),
    path('viewall/',views.patient_list,name='patient_list'),
    path('view/<fetchid>',views.patient_details,name='patient_details'),
    path('pcode/<fetchpatient_code>',views.patient_search,name='patient_search'),
    path('',views.patient_interface,name='patient_interface'),

]