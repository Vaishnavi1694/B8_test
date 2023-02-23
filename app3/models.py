from django.db import models
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    department = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    email = models.EmailField(null = True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f"{self.name} ---{self.address}"

    def show_details(self):
        print(f'''
Employee Name:- {self.name}
Employee Age:- {self.age}
Employee Mobile No:- {self.mobile_num}
Employee Address:- {self.address}''')