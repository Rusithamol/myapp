
from django.urls import path
from .views import*  

urlpatterns = [
    path('PatientRegistrationpage/',patient_registration_page,name="patient"),
    path('DonarRegistrationpage/',donar_registration_page,name='donor'),
    path('patienttable/',patienttable),
    path('donartable/',donartable)

    
   
]


