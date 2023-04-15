from django.conf.urls import url
from PTapp import views

urlpatterns = [
    url(r'bus$',views.BusAPI),
    url(r'^bus/([0-9]+)$',views.BusAPI),

    url(r'^trip$',views.TripAPI) ,
    url(r'^trip/([0-9]+)$',views.TripAPI),

    
    url(r'^employee$',views.EmployeeAPI) ,
    url(r'^employee/([0-9]+)$',views.EmployeeAPI),

    url(r'^ticket$',views.TicketAPI) ,
    url(r'^ticket/([0-9]+)$',views.TicketAPI),
]