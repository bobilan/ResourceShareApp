from django.db import models


class CreatedModifiedDateTimeBase(models.Model):
    created_at= models.DateTimeField(auto_now_add=True) # will be created just once
    modified_at= models.DateTimeField(auto_now=True) # will be updated each time 
    
    class Meta:
        abstract = True