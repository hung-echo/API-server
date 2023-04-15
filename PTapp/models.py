from django.db import models

# Create your models here.

class Bus(models.Model):
    # Thông tin về xe bao gồm: số xe khách(ID của xe), hãng, kiểu xe, số lượng chỗ ngồi
    id = models.AutoField(primary_key = True)
    Brand = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Capacity = models.IntegerField()

class Trip(models.Model):
    """Thông tin về chuyến đi bao gồm: Id chuyến đi(khoá chính), 
    Id xe khách(khoá ngoại), điểm bắt đầu, điểm kết thúc,
    ngày và giờ khởi hành, ngày và giờ điểm đến"""
    id = models.IntegerField(primary_key = True)
    busId = models.ForeignKey(Bus, on_delete = models.CASCADE)
    StartPoint = models.CharField(max_length = 100)
    StartDate = models.DateTimeField()
    EndPoint = models.CharField(max_length = 100)
    EndDate = models.DateTimeField()

class Employee(models.Model):
    """Thông tin nhân viên bao gồm:ID nhan vien, tên nhân viên,
      số điện thoại, vị trí công việc, lương, tài khoản(khoá chính), mật khẩu"""
    id = models.AutoField(primary_key = True)
    Username = models.EmailField()
    Password = models.CharField(max_length = 100)
    EmployeeName = models.CharField(max_length= 200)
    EmployeePhone = models.IntegerField()
    EmployeePosition = models.CharField(max_length=100)
    Salary = models.FloatField()
    
class Branch(models.Model):
    """Thông tin về chi nhánh bao gồm: mã chi nhánh(khoá chính), 
    tên chi nhánh, mã nhân viên(khoá ngoại)"""
    id = models.CharField(primary_key = True, max_length = 10)
    BranchName = models.CharField(max_length = 100)
    employeeId = models.ForeignKey(Employee, on_delete = models.CASCADE)

class Ticket(models.Model):
    """Thông tin vé xe bao gồm: Id vé(khoá chính), Id của chuyến đi(khoá ngoại),
      Id nhân viên(khoá ngoại),vị trí ghế, giá vé, ngày mua, 
      phương thức thanh toán, số điện thoại, tên hành khách"""
    id = models.AutoField(primary_key = True)
    tripId = models.ForeignKey(Trip, on_delete = models.CASCADE)
    employeeId = models.ForeignKey(Employee, on_delete = models.CASCADE)
    PassengerName = models.CharField(max_length=200)
    PassengerPhone = models.IntegerField()
    SeatNumber = models.IntegerField()
    Price = models.FloatField()
    Payment = models.CharField(max_length=200)
    DateOfPurchase = models.DateTimeField()