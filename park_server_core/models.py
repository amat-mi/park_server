# coding: utf-8

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


#################################################
class Status(models.Model):
  stamp = models.DateTimeField(null=False, auto_now_add=True)
  nowstamp = models.DateTimeField(null=True,blank=True)
  webstamp = models.DateTimeField(null=True,blank=True)
  capacity = models.IntegerField(null=False, default=0)
  full = models.IntegerField(null=False, default=0)
  free = models.IntegerField(null=False, default=0)

  class Meta:
    ordering = ['stamp']
    abstract = True

#################################################
class ParkData(Status):
  park = models.ForeignKey('Park', related_name='data', null=False, on_delete=models.CASCADE)  

  class Meta:
    verbose_name = "Dati parcheggio"
    verbose_name_plural = "Dati parcheggio"
    ordering = ['park','stamp']

@receiver(post_save, sender=ParkData)
def post_save_ParkData(sender, instance, created, *args, **kwargs):
  u"""
  Dopo la creazione di un dato di parcheggio, chiama la refresh sul parcheggio per ricalcolare lo status corrente 
  """
  if created:
    instance.park.update_status(instance)        

#################################################
class ParkStatus(Status):
  park = models.OneToOneField('Park', related_name='status', null=False, on_delete=models.CASCADE)  

  class Meta:
    verbose_name = "Stato parcheggio"
    verbose_name_plural = "Stati parcheggio"
    ordering = ['park','stamp']

  def copy_from_parkdata(self,parkdata):
    self.stamp = parkdata.stamp
    self.nowstamp = parkdata.nowstamp
    self.webstamp = parkdata.webstamp
    self.capacity = parkdata.capacity
    self.full = parkdata.full
    self.free = parkdata.free
    self.park = parkdata.park
    self.full_clean()
    self.save()    
  
#################################################
class Park(models.Model):
  title = models.CharField(max_length=80, null=False, unique=True)

  def __unicode__(self):
    return u'{}'.format(self.title)  
  
  class Meta:
    verbose_name = "Parcheggio"
    verbose_name_plural = "Parcheggi"
    ordering = ['title']
  
  def update_status(self,parkdata):
    try:
      status = self.status
    except ObjectDoesNotExist:
      status = ParkStatus()
    status.copy_from_parkdata(parkdata)
    status.full_clean()
    status.save()    
    self.status = status
    self.full_clean()
    self.save()    
