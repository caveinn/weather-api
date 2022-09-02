from rest_framework import serializers


class TemparatureSerializer(serializers.Serializer):
    '''Temparature data serializer class'''
    city = serializers.CharField(
        write_only=True,
        max_length=60,
        required=True,
        allow_null=False,
    )

    number_of_days = serializers.IntegerField(
        write_only=True,
        min_value=1,
        max_value=10,
        required=True,
        allow_null=False,
    )

    maximum = serializers.FloatField(read_only=True)
    minimum = serializers.FloatField(read_only=True)
    avarage = serializers.FloatField(read_only=True)
    median = serializers.FloatField(read_only=True)
