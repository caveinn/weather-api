from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import Response


from .helpers import weather_api_helper
from .serializers import TemparatureSerializer


class TemperatureAPIView(RetrieveAPIView):
    '''Class to handle temperature stats retrieval'''
    permission_classes = (AllowAny,)
    serializer_class = TemparatureSerializer

    def get(self, request, city):
        """
        override the get method to get weather stats
        Args:
            request: (obj) request object
            city: (str) city name
        Returns:
            (obj) response object containing the city weather stats
        """
        data = {'city': city, 'number_of_days': request.query_params.get(
            'number_of_days')}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        temparature_data = weather_api_helper.get_temperature_data(
            city, data.get('number_of_days')
        )
        return Response(data=temparature_data)
