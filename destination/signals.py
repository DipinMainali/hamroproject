from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Destimages,Place_rating,Places,Comment,Hotel

@receiver(post_save,sender=Places)
def create_hotel_objects(sender,instance,created,**kwargs):
    if created:
     Hotel.objects.create(nearby=instance)
def update_hotel(sender,instance,**kwargs):
    instance.hotel.save()    

@receiver(post_save,sender=Places)
def create_destimages(sender,instance,created,**kwargs):
    if created:
        Destimages.objects.create(place=instance)
def update_images(sender,instance,**kwargs):
    instance.destimages.save()    

