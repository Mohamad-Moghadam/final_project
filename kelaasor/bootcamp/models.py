from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point

class BootCamps(models.Model):
    BOOTCAMPS= ['Back-End', 'Front-End', 'Full-Stack', 'Social Media', 'Product Management', 'Data Science', 'Cyber Security', 'UI/UX', 'Mobile Development', 'Game Development']
    title= models.Choices(*BOOTCAMPS)
    description= models.TextField()
    teachers= models.ManyToManyField(User, related_name= 'Teachers_of_a_bootcamp')
    students= models.ManyToManyField(User, related_name= 'Students_of_a_bootcamp')
    starting_date= models.DateField(blank= True, null= True)
    ending_date= models.DateField(blank= True, null= True)
    created_at= models.DateTimeField(auto_now_add= True)
    location= gis_models.PointField(default= Point(35.69967769328554,51.31804375220537))
    price= models.BigIntegerField()
    enrollment_status= models.BooleanField(default= True)

    class Meta:
        verbose_name= 'Bootcamp'
        verbose_name_plural= 'Bootcamps'

class BootcampRequest(models.Model):
    user= models.ForeignKey(User, on_delete= models.PROTECT, related_name= "user_that_asked_for_enrollment")
    bootcamp= models.ForeignKey(BootCamps, on_delete= models.PROTECT)