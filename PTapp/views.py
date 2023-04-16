from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PTapp.models import Bus,Ticket,Employee,Trip,Branch
from PTapp.serializers import BusSerializer,TicketSerializer,TripSerializer,BranchSerializer,EmployeeSerializer
# Create your views here
@csrf_exempt
def BusAPI(request, id = 0):
    if request.method == 'GET':
        buses = Bus.objects.all()
        buses_serializer = BusSerializer(buses, many = True)
        return JsonResponse(buses_serializer.data, safe= False)
    elif request.method == 'POST':
        bus_data = JSONParser().parse(request)
        bus_serializer = BusSerializer(data = bus_data)
        if bus_serializer.is_valid():
            bus_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failded to add", safe= False)
    elif request.method == 'PUT':
        bus_data = JSONParser().parse(request)
        bus = Bus.objects.get(id = bus_data['id'])
        bus_serializer = BusSerializer(bus, data= bus_data)
        if bus_serializer.is_valid():
            bus_serializer.save()
            return JsonResponse("Update Successfully", safe = False)
        return JsonResponse("Update Faild", safe= False)
    elif request.method == 'DELETE':
        bus = Bus.objects.get(id = id)
        bus.delete()
        return JsonResponse("Deleted", safe= False)

@csrf_exempt
def TripAPI(request, id = 0):
    if request.method == 'GET':
        trip = Trip.objects.all()
        trip_serializer = TripSerializer(trip, many = True)
        return JsonResponse(trip_serializer.data, safe= False)
    elif request.method == 'POST':
        trip_data = JSONParser().parse(request)
        trip_serializer = TripSerializer(data = trip_data)
        if trip_serializer.is_valid():
            trip_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failded to add", safe= False)
    elif request.method == 'PUT':
        trip_data = JSONParser().parse(request)
        trip = Trip.objects.get(id = trip_data['id'])
        trip_serializer = TripSerializer(trip, data = trip_data)
        if trip_serializer.is_valid():
            trip_serializer.save()
            return JsonResponse("Update Successfully", safe = False)
        return JsonResponse("Update Faild", safe = False)
    elif request.method == 'DELETE':
        trip = Trip.objects.get(id = id)
        trip.delete()
        return JsonResponse("Deleted", safe = False)

@csrf_exempt
def EmployeeAPI(request, id = 0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee, many = True)
        return JsonResponse(employee_serializer.data, safe= False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failded to add", safe= False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(id = employee_data['id'])
        employee_serializer = EmployeeSerializer(employee, data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfully", safe = False)
        return JsonResponse("Update Faild", safe = False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(id = id)
        employee.delete()
        return JsonResponse("Deleted", safe = False)

@csrf_exempt
def TicketAPI(request, id = 0):
    if request.method == 'GET':
        ticket = Ticket.objects.all()
        ticket_serializer = TicketSerializer(ticket, many = True)
        return JsonResponse(ticket_serializer.data, safe= False)
    elif request.method == 'POST':
        ticket_data = JSONParser().parse(request)
        ticket_serializer = TicketSerializer(data = ticket_data)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failded to add", safe= False)
    elif request.method == 'PUT':
        ticket_data = JSONParser().parse(request)
        ticket = Ticket.objects.get(id = ticket_data['id'])
        ticket_serializer = TicketSerializer(ticket, data = ticket_data)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse("Update Successfully", safe = False)
        return JsonResponse("Update Faild", safe = False)
    elif request.method == 'DELETE':
        ticket = Ticket.objects.get(id = id)
        ticket.delete()
        return JsonResponse("Deleted", safe = False)
