from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import Response
from .helpers import weather_api_helper

class TemperatureAPIView(RetrieveAPIView):
    '''Class to handle temperature stats retrieval'''
    permission_classes = (AllowAny,)
    
    def get(self, request, city):
        data = {'city': city, 'days': request.query_params.get('number_of_days')}
        temparature_data = weather_api_helper.get_temperature_data(data.get('city'), data.get('days'))
        return Response(data=temparature_data)