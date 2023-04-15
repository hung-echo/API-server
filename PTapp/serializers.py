from rest_framework import serializers
from PTapp.models import Bus, Employee, Ticket, Trip, Branch 

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id','Brand','Type','Capacity')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','Username','Password','EmployeeName','EmployeePhone','EmployeePosition','Salary')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','PassengerName','PassengerPhone','SeatNumber','Price','Payment','DateOfPurchase','employeeId','tripId')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id','BranchName','employeeId')

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id','StartPoint','StartDate','EndPoint','EndDate', 'busId')
              