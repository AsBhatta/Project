from rest_framework import serializers
from .models import user_profile

class profileserializer(serializers.ModelSerializer):

    class Meta:
        model = user_profile
        fields = '__all__'