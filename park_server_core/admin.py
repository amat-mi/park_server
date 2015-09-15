# coding: utf-8

from django.contrib import admin

from models import Park


#################################################
class BaseAdmin(admin.ModelAdmin):
  save_on_top = True    

#################################################
class ParkAdmin(BaseAdmin):
  pass
admin.site.register(Park,ParkAdmin)
