import json
from unittest.mock import patch

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status


class TestWeatherStats(APITestCase):
    """
    Api test cases
    """

    def setUp(self):
        """
        Setup base test variables
        """
        self.base_url = reverse('temparature-stats',
                                kwargs={"city": "Nairobi"})
        self.days_query_params = {'number_of_days': 2}
        self.sample_weather_api_repsonse = ''
        with open('app/api/MockData/weather_api_reponse.json', 'r') \
                as sample_response_file:
            self.sample_weather_api_repsonse = json.loads(
                sample_response_file.read())

    def test_missing_number_of_days_fails(self):
        """
        Fetch city weather stats with invalid days fails
        """

        response = self.client.get(self.base_url, format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data, dict)
        self.assertIn('This field may not be null',
                      data['errors']['number_of_days'][0])

    def test_too_many_days_fails(self):
        response = self.client.get(self.base_url, {"number_of_days": 15},
                                   format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data, dict)
        self.assertIn('Ensure this value is less than or equal to 10',
                      data['errors']['number_of_days'][0])

    @patch('app.api.views.weather_api_helper.get_weather_stats')
    def test_get_weather_stats_gets_called(self, mocked_function):
        mocked_function.return_value = self.sample_weather_api_repsonse
        response = self.client.get(self.base_url, self.days_query_params,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_function.called)
        self.assertTrue(mocked_function.called_with('Nairobi', 2))

    @patch('app.api.views.weather_api_helper.get_weather_stats')
    def test_returns_accurate_information(self, mocked_function):
        mocked_function.return_value = self.sample_weather_api_repsonse
        response = self.client.get(self.base_url, self.days_query_params,
                                   format='json')
        data = response.data
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('maximum'), 24.0)
        self.assertEqual(data.get('minimum'), 12.7)
        self.assertEqual(data.get('average'), 17.89)
        self.assertEqual(data.get('median'), 18.3)
