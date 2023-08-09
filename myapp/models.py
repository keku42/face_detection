from django.db import models

# Create your models here.
class employee(models.Model):
    # id=models.CharField(max_length=3,primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    contect = models.CharField(max_length=15)
    email = models.EmailField()

    def _str_(self):
        return self.name
    
    class Meta:
        db_table = 'employee'

class attendance_table(models.Model):
    emp_id = models.ForeignKey(employee,on_delete=models.CASCADE,db_column='emp_id')
    Date = models.DateField()
    Time = models.TimeField()
    Type = models.CharField(max_length=15)

    def _str_(self):
        return f'{self.emp_id} - {self.Date} - {self.Time}  -{self.Type}'
    
    class Meta:
        db_table = 'attendance_table'
