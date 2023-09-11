from rest_framework import serializers
from accounts.models import CustomUser

from .models import Event,EventMembers,Gallery,Activites

# Create Event Serializer 
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

class EventMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMembers
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ActivitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activites
        fields = '__all__'






