from django.contrib import admin

from .models import Station

class StationAdmin(admin.ModelAdmin):
    list_display= ('name', 'bikes_count', 'terminal_id')


admin.site.register(Station, StationAdmin)
