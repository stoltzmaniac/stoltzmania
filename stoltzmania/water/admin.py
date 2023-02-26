from django.contrib.gis import admin
from .models import SurfaceWaterStation

admin.site.register(SurfaceWaterStation, admin.ModelAdmin)
