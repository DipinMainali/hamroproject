from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Destimagesfile,Place_rating,Places,Comment,Hotel

@receiver(post_save,sender=Places)
def create_hotel_objects(sender,instance,created,**kwargs):
    if created:
     Hotel.objects.create(nearby=instance)


@receiver(post_save,sender=Places)
def create_destimages(sender,instance,created,**kwargs):
    if created:
        Destimagesfile.objects.create(place=instance)

