from django.contrib import admin
from datalogger.models import Filling, LogEntry


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('timestamp','ip','rssi','humidity','temp','millis','distance')
#    list_filter = ('site',)

class FillingAdmin(admin.ModelAdmin):
    list_display = ('timestamp',)
#    list_filter = ('device_timezone',)
    
admin.site.register(Filling, FillingAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
