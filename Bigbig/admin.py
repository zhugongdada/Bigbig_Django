from django.contrib import admin
from Bigbig.models import Guest


# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'create_time']


admin.site.register(Guest, GuestAdmin)
