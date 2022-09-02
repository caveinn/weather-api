from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema

from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import Response
from rest_framework.decorators import action


from .helpers import weather_api_helper
from .serializers import TemparatureSerializer


class TemperatureAPIView(RetrieveAPIView):
    '''Class to handle temperature stats retrieval'''
    permission_classes = (AllowAny,)
    serializer_class = TemparatureSerializer
    days_request_param = openapi.Parameter(
        'number_of_days', openapi.IN_QUERY,
        description="number of days to get weather stats",
        type=openapi.TYPE_INTEGER,
        required=True)

    @swagger_auto_schema(method='get',
                         manual_parameters=[days_request_param])
    @action(methods=['GET'], detail=True)
    def get(self, request, city):
        '''
        override the get method to get weather stats
        Args:
            request: (obj) request object
            city: (str) city name
        Returns:
            (obj) response object containing the city weather stats
        '''
        data = {'city': city, 'number_of_days': request.query_params.get(
            'number_of_days')}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        temparature_data = weather_api_helper.get_temperature_data(
            city, data.get('number_of_days')
        )
        return Response(data=temparature_data)
