from rest_framework import serializers
from needs.models import Need



class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = ('__all__')