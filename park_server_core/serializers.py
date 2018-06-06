# coding: utf-8

from rest_framework import serializers

from .models import Park, ParkStatus, ParkData


#################################################
class ParkStatusSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = ParkStatus
    exclude = ['id','park']

#################################################
class ParkSerializer(serializers.ModelSerializer):
  status = ParkStatusSerializer(read_only=True)

  class Meta:
    model = Park
    fields = ['pk','title','status']

#################################################
class ParkDataSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = ParkData
    fields = '__all__'
