from django.contrib.auth.models import User

from rest_framework import serializers

from ridecell.alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()

    class Meta:
        model = Alert
        fields = ('user', 'id', 'location', 'radius', 'time_start', 'time_end')
        read_only_fields = ('location',)

    def validate(self, data):
        """
        Check that the start is before the end.
        """
        if data['time_start'] > data['time_end']:
            raise serializers.ValidationError("end must occur after start")

        return data
