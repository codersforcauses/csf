from django.contrib import admin
from .models import Event
from .views import export_eventcsv

export_eventcsv.short_description = "Export as CSV"

class EventModelAdmin(admin.ModelAdmin):
    actions = [export_eventcsv]


# Register your models here.
# admin.site.register(Event)
admin.site.register(Event, EventModelAdmin)
