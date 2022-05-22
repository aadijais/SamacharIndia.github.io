from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    mobno=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    msg=models.CharField(max_length=300)
    def __str__(self):
        return self.email

class category(models.Model):
    cname=models.CharField(max_length=120)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()
    def __str__(self):
        return self.cname

class city(models.Model):
    city=models.CharField(max_length=300)
    cdate=models.DateField()
    def __str__(self):
        return self.city

class news(models.Model):
    ncity=models.ForeignKey(city,on_delete=models.CASCADE)
    nhead=models.CharField(max_length=1000)
    ncategory=models.ForeignKey(category,on_delete=models.CASCADE)
    nsubject=models.CharField(max_length=200)
    ndes=HTMLField()
    ndate=models.DateField()
    npic=models.ImageField(upload_to='static/news/', default="")

class videonews(models.Model):
    vlink=models.CharField(max_length=600)
    vtitle=models.TextField(max_length=1000)
    vnews=HTMLField()
    vcity=models.ForeignKey(city,on_delete=models.CASCADE)
    vcategory=models.ForeignKey(category,on_delete=models.CASCADE)
    vdate=models.DateField()



class notification(models.Model):
    ndes=models.TextField(max_length=1000)
    ndate=models.DateField()

class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider/',default="")
    stitle=models.CharField(max_length=500)
    sdes=models.TextField(max_length=2000)
    sdate=models.DateField()






