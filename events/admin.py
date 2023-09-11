from django.contrib import admin

# Register your models here.
from .models import Event,EventMembers,Gallery,Activites

class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields] 
    list_filter = ['event_name']
    list_per_page = 20
    ordering = ['id']

class EventMembersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventMembers._meta.fields]
    list_filter = ['event_id']
    list_per_page = 20
    ordering = ['id']

admin.site.register(Event,EventAdmin)

admin.site.register(EventMembers,EventMembersAdmin)   

admin.site.register(Gallery)

admin.site.register(Activites)