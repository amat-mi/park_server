# coding: utf-8

from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Park, ParkData
from .serializers import ParkSerializer, ParkDataSerializer


#################################################
def build_message_response(message,status=HttpResponse.status_code):
  return Response({'message': message},status=status)

#################################################
class RESPERR(object):
  GENERIC_ERROR = 'GENERIC_ERROR'

def build_error_response(error,status=HttpResponseBadRequest.status_code,message=None):
  return Response({'error': error, 'message': message},status=status)

#################################################
def build_exception_response(error=RESPERR.GENERIC_ERROR,status=HttpResponseBadRequest.status_code):
    import traceback
    return build_error_response(error,status,message=traceback.format_exc())

#################################################
class ParkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ParkSerializer
    queryset = Park.objects.all()
    paginate_by = None

#################################################
class ParkDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ParkDataSerializer
    queryset = ParkData.objects.all().order_by('pk',)
    paginate_by = None

    def get_queryset(self):
        res = super(ParkDataViewSet,self).get_queryset()
        last_pk = self.request.query_params.get('last_pk',None)
        return res.filter(pk__gt=last_pk) if last_pk else res
 
    @list_route(methods=['PUT'])
    def upload(self, request):
      try:          
          (park,created) = Park.objects.get_or_create(title=request.data['name'])
          request.data['park'] = park.pk
          serializer_class = self.get_serializer_class()  
          serializer = serializer_class(data=request.data, many=False, partial=True)
          if serializer.is_valid():
              serializer.save()                                                
              return build_message_response('OK')
          else:
              return build_error_response(serializer.errors)
      except Exception as exc:
          return build_exception_response()
         