from django.db import connections
from django.db import models
from django.utils import timezone


class departments(models.Model):

    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)

    class Meta:
        db_table = "department"


class course(models.Model):

    Name = models.CharField(max_length=250)
    CID = models.CharField(max_length=250)
    prerequisites = models.CharField(max_length=250)
    DID = models.CharField(max_length=250)

    class Meta:
        db_table = "course"


class dep(models.Model):

    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)


# Create your models here.
