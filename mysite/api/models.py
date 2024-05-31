from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class DoctorDetail(AbstractBaseUser):
    Admin_ID = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    User_Name = models.EmailField(max_length=100)  
    password = models.CharField(max_length=128) 
    Birth_Date = models.DateField()  
    Gender = models.CharField(max_length=10) 
    Phone = models.IntegerField()  

    def __str__(self):
        return f"{self.First_Name} {self.Middle_Name} {self.Last_Name} "
