from rest_framework import serializers


class TemparatureSerializer(serializers.Serializer):
    '''Temparature data serializer calss'''
    city = serializers.CharField(
        max_length=60,
        required=True,
        allow_null=False,
    )

    number_of_days = serializers.IntegerField(
        min_value=1,
        max_value=10,
        required=True,
        allow_null=False,
    )
