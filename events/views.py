from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import Event,EventMembers,Gallery,Activites
from .serializers import EventSerializer,EventMembersSerializer,GallerySerializer,ActivitesSerializer

#Perform Event CRUD operations
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def event_operations(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        final_data = {}
        if id is not None:
            event = Event.objects.get(id=id)
            serializer = EventSerializer(event)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            user_id = request.user
            try:
                events_data = Event.objects.filter(Q(event_members__user_id=user_id)&Q(active=True))
                #print("Events Data: {}".format(events_data))
                serializer = EventSerializer(events_data,many=True)
                final_data["accessed_events"] = serializer.data
                return Response(final_data,status=status.HTTP_200_OK)
            except Event.DoesNotExist:
                return Response("No events found",status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "POST":
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "PUT":
        id = request.data.get("id",None)
        try:
            event_data = Event.objects.get(id=id)
            serializer = EventSerializer(event_data,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Event.DoesNotExist:
            return Response("Select event id",status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        id = request.GET.get("id",None)
        try:
            event_data = Event.objects.get(id=id)
            event_data.active = False
            event_data.save()
            return Response("Event removed successfully",status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response("Some thing went wrong conatct Admin",status=status.HTTP_400_BAD_REQUEST)
        

#Perform Event Members CRUD operations
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def event_members_operations(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id is not None:
            event_members = EventMembers.objects.get(id=id)
            serializer = EventMembersSerializer(event_members)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("Select member id",status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "POST":
        try:
            event_member = EventMembers.objects.get(Q(user_id=request.data.get('user_id'))&Q(active=True)&Q(event_id=request.data.get('event_id')))
            if not event_member.active:
                event_member.active = True
                event_member.save()
        except:
            serializer = EventMembersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "PUT":
        id = request.data.get("id",None)
        try:
            event_members_data = EventMembers.objects.get(id=id)
            serializer = EventMembersSerializer(event_members_data,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except EventMembers.DoesNotExist:
            return Response("Select member id",status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        id = request.GET.get("id",None)
        try:
            event_members_data = EventMembers.objects.get(id=id)
            event_members_data.active = False
            event_members_data.save()
            return Response("Member removed successfully",status=status.HTTP_200_OK)
        except EventMembers.DoesNotExist:
            return Response("Some thing went wrong conatct Admin",status=status.HTTP_400_BAD_REQUEST)
        
# Perform Gallery CRUD operations
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def gallery_operations(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        event_id = request.GET.get('event',None)
        if id is not None:
            gallery = Gallery.objects.get(id=id)
            serializer = GallerySerializer(gallery)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif event_id is not None:
            gallery_data = Gallery.objects.filter(Q(active=True)&Q(event_id=event_id))
            print("Gallery Data: {}".format(gallery_data))
            serializer = GallerySerializer(gallery_data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("Select gallery event",status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "POST":
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "PUT":
        id = request.data.get("id",None)
        try:
            gallery_data = Gallery.objects.get(id=id)
        except:
            return Response("Data not found",status=status.HTTP_400_BAD_REQUEST)
        serializer = GallerySerializer(gallery_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        id = request.GET.get("id",None)
        try:
            gallery_data = Gallery.objects.get(id=id)
            gallery_data.active = False
            gallery_data.save()
            return Response("Photo deleted",status=status.HTTP_200_OK)
        except:
            return Response("data not found",status=status.HTTP_400_BAD_REQUEST)

# Perform Activities CRUD operations
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def activities_operations(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        event_id = request.GET.get('event',None)
        if id is not None:
            activities = Activites.objects.get(id=id)
            serializer = ActivitesSerializer(activities)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif event_id is not None:
            activities_data = Activites.objects.filter(Q(active=True)&Q(event_id=event_id))
            serializer = ActivitesSerializer(activities_data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("Select activity id",status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "POST":
        serializer = ActivitesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        id = request.data.get("id",None)
        activity_data = Activites.objects.get(id=id)
        serializer = ActivitesSerializer(activity_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        id = request.GET.get("id",None)
        try:
            activity_data = Activites.objects.get(id=id)
            activity_data.active = False
            activity_data.save()
            return Response("Activity removed successfully",status=status.HTTP_200_OK)
        except Activites.DoesNotExist:
            return Response("Some thing went wrong conatct Admin",status=status.HTTP_400_BAD_REQUEST)






