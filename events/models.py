from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Event(models.Model):
    event_name        = models.CharField(max_length=100)
    event_description = models.TextField(max_length=100)
    event_pic         = models.TextField(blank=True,null=True)
    event_start_date  = models.DateField()
    event_end_date    = models.DateField(blank=True,null=True)
    active            = models.BooleanField(default=True)

    def __str__(self):
        return self.event_name
    
MEMBER_ROLES = (("ADMIN", "ADMIN"),("MANAGER", "MANAGER"),("VOLUNTEER", "VOLUNTEER"))
MEMBER_ADDED_ROLES = (("ADMIN", "ADMIN"),("MANAGER", "MANAGER"),("INVITED", "INVITED"))
ACTIVITY_STATUS = (("ON_GOING", "ON_GOING"),("UP_COMING","UP_COMING"),("COMPLETED","COMPLETED"))

class EventMembers(models.Model):
    event_id      = models.ForeignKey(Event, on_delete=models.CASCADE,related_name="event_members")
    user_id       = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role          = models.CharField(max_length=10, choices=MEMBER_ROLES,default="VOLUNTEER")
    added_through = models.CharField(max_length=10,choices=MEMBER_ADDED_ROLES,default="MANAGER")
    added_by      = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="event_members_added_by")
    created_at    = models.DateField(auto_now_add=True)
    active        = models.BooleanField(default=True)

class Gallery(models.Model):
    image = models.TextField()
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

class Activites(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    activity_at = models.DateTimeField()
    status = models.CharField(max_length=10, choices=ACTIVITY_STATUS,default="UP_COMING")
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
