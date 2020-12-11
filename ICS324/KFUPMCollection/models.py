from django.db import connections
from django.db import models
from django.utils import timezone


class departments(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    DID = models.CharField(max_length=250, primary_key=True, unique=True)

    class Meta:
        db_table = "department"


class course(models.Model):
    Name = models.CharField(max_length=250)
    CID = models.CharField(max_length=250, unique=True)
    prerequisites = models.CharField(max_length=250)
    DID = models.CharField(max_length=250)

    class Meta:
        db_table = "course"

class student(models.Model):
    SID = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250, null=False, blank=False, unique=True)
    Major = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        db_table = "student"

class instructor(models.Model):
    IID = models.CharField(max_length=250, primary_key=True, unique=True)
    DID = models.ForeignKey(departments, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250, null=False, blank=False, unique=True)
    Office_Phone_number = models.CharField(max_length=250)
    Office_location = models.CharField(max_length=250)
    website = models.URLField(max_length=250)

    class Meta:
        db_table = "instructor"


class evaluation(models.Model):
    EID = models.CharField(max_length=250, primary_key=True, unique=True)
    Comment = models.CharField(max_length=500)
    E_Date = models.DateTimeField(auto_now_add=True)
    SID = models.ForeignKey(student, on_delete=models.SET_NULL, null=True, blank=True)
    IID = models.ForeignKey(instructor, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "evaluation"

class resource(models.Model):
    RID = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    CID = models.ForeignKey(course, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "resource"

class question(models.Model):
    QID = models.CharField(max_length=250, primary_key=True, unique=True)
    Qname = models.CharField(max_length=250)
    Weight = models.IntegerField(default=0)

    class Meta:
        db_table = "question"

class answer(models.Model):
    AID = models.CharField(max_length=250, primary_key=True, unique=True)
    Rate = models.IntegerField(default=0)
    QID = models.ForeignKey(question, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "answer"


class teach(models.Model):
    CID = models.ForeignKey(course, on_delete=models.SET_NULL, null=True, blank=True)
    IID = models.ForeignKey(instructor, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "teach"

class contains(models.Model):
    QID = models.ForeignKey(question, on_delete=models.SET_NULL, null=True, blank=True)
    EID = models.ForeignKey(evaluation, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "contains"

# Create your models here.