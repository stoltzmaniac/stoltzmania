from django.contrib.gis.db import models


class SurfaceWaterStation(models.Model):
    """
    Stores a single surface water station
    :model:`water.SurfaceWaterStation`.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    div = models.IntegerField(null=True)
    wd = models.IntegerField(null=True)
    county = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=50, null=True)
    station_name = models.CharField(max_length=500, null=True)
    dwr_abbrev = models.CharField(max_length=50, null=True)
    usgs_station_id = models.IntegerField(null=True)
    data_source = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    por_start = models.IntegerField(null=True)
    por_end = models.IntegerField(null=True)
    utm_x = models.IntegerField(null=True)
    utm_y = models.IntegerField(null=True)
    location_accuracy = models.CharField(max_length=500, null=True)
    more_information = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=500, null=True)
    geometry = models.PointField(srid=4326, null=True, spatial_index=True)

    def __str__(self):
        return f"Station: {self.station_name} -- {self.county}, {self.state}"
