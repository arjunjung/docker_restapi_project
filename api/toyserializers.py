from rest_framework import serializers
from api.models import ToyModel

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToyModel
        fields = ['id','name','description','category','price','was_included_in_home',]