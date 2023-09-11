from django.urls import path
from .views import event_operations,event_members_operations,gallery_operations


urlpatterns = [
    path('add_event/', event_operations, name='add_event'),
    path('edit_event/', event_operations, name='edit_event'),
    path('delete_event/', event_operations, name='delete_event'),
    path('get_event/', event_operations, name='get_event'),

    path('add_event_member/', event_members_operations, name='add_event_member'),
    path('edit_event_member/', event_members_operations, name='edit_event_member'),
    path('delete_event_member/', event_members_operations, name='delete_event_member'),
    path('get_event_members/', event_members_operations, name='get_event_members'),

    path('add_image/', gallery_operations, name='add_gallery'),
    #path('edit_image/', gallery_operations, name='edit_gallery'),
    path('delete_image/', gallery_operations, name='delete_gallery'),
    path('get_images/', gallery_operations, name='get_gallery'),
]