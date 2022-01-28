
from django.db import models
import datetime
from django.contrib.auth.models import User

from django.utils import timezone



   

class Places(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=True,blank=True)
    address=models.CharField(max_length=30)
    descrption=models.TextField()
    thumbnail_image=models.ImageField(upload_to="images",null=True,blank=True)
    

    def __str__(self):
        return self.name
    
class Place_rating(models.Model):
    rate=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)],default=0)
    place=models.ForeignKey(Places,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Comment(models.Model):
    place=models.ForeignKey(Places,related_name="review",on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    comment_body= models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' %(self.place.name,self.name)


class Destimages(models.Model):
    place=models.ForeignKey(Places,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.place.name



class Hotel(models.Model):
    title=models.CharField(max_length=20)
    contact_info=models.CharField(max_length=15)
    nearby=models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return self.nearby.name







        





