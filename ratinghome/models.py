from django.db import models
# Create your models here.
class rateinfo(models.Model):
    pID=models.IntegerField(primary_key=True)
    pName=models.CharField(max_length=30)
    rating_choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
    culture=models.IntegerField(choices=rating_choices)
    adventure=models.IntegerField(choices=rating_choices)
    wildlife=models.IntegerField(choices=rating_choices)
    sightseeing=models.IntegerField(choices=rating_choices)
    history=models.IntegerField(choices=rating_choices)
    tag_title=models.CharField(max_length=200)
    province_choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)]
    province=models.IntegerField(choices=province_choices)
    
    def __str__(self):
        return self.pName
    class meta:
        ordering=['-pID']
        






