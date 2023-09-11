from django.apps import AppConfig
from django.contrib import admin
from .models import CustomUser

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals

@admin.register(CustomUser)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')