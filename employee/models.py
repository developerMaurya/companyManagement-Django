from django.db import models

# Create your models here.
class empregistration(models.Model):
    empid=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    workrole=models.CharField(max_length=20)
    emp_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
#------------------------------------------------------------
# Create your models here.
class stprofile1(models.Model):
    student_id=models.CharField(max_length=20,primary_key=True)
    student_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
    student_course1=models.CharField(max_length=20)
    student_course2=models.CharField(max_length=20)
    student_course3=models.CharField(max_length=20)
    student_course4=models.CharField(max_length=20)
    full_marks=models.IntegerField()
    obtaind_marks=models.IntegerField()
    grad=models.CharField(max_length=20)
    percentage=models.CharField(max_length=20)
    stdimage=models.ImageField()
#-----------------------------------------------------------------
class stperformance(models.Model):
    student_id=models.CharField(max_length=20,primary_key=True)
    student_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    mobile=models.IntegerField()
    full_marks=models.IntegerField()
    obtaind_marks=models.IntegerField()
    grad=models.CharField(max_length=20)
    percentage=models.CharField(max_length=20)
    attendance=models.CharField(max_length=20)
    student_type=models.CharField(max_length=20)
    performance=models.CharField(max_length=20)
    studimage=models.ImageField()
#--------------------------------------------------------------
class studentperformance(models.Model):
    studentsid=models.CharField(max_length=20,primary_key=True)
    student_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    mobile=models.IntegerField()
    full_marks=models.IntegerField()
    obtaind_marks=models.IntegerField()
    grad=models.CharField(max_length=20)
    percentage=models.CharField(max_length=20)
    attendance=models.CharField(max_length=20)
    student_type=models.CharField(max_length=20)
    performance=models.CharField(max_length=20)
    studimage=models.ImageField()