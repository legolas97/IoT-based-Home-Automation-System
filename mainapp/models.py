from django.db import models
from django.contrib.auth.models import User
import datetime,os
class RelayGroup(models.Model):

    r_name = models.CharField(max_length=100,blank=True,null=True,unique=True)
    r_status = models.BooleanField(default=False)
    r_lastupdateinfo = models.DateTimeField(default= datetime.datetime.now())
    #ow_phone_store = models.CharField(max_length=30, blank=True, null=True)
    #ow_phone_store_sec = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.r_name
    class Meta:
        db_table = 'RelayGroup'

