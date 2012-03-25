from planes.models import Fleet, Plane
from django.contrib import admin
#from cms.admin.placeholderadmin import PlaceholderAdmin

class FleetInline(admin.StackedInline):
    model = Plane
    
class FleetAdmin(admin.ModelAdmin):
    inlines = [FleetInline,]

    
admin.site.register( Fleet, FleetAdmin )