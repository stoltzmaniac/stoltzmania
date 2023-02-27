from django.contrib.gis import forms
from stoltzmania.water.models import SurfaceWaterStation


class SurfaceWaterStationForm(forms.ModelForm):
    
    point = forms.PointField(srid=4326, 
                widget=forms.OSMWidget(
                    attrs={
                        "map_width": 800,
                        "map_srid": 4326,
                        "map_height": 500,
                        "default_lat": 49.246292,
                        "default_lon": -123.116226,
                        "default_zoom": 7,
                        }
                    ),
                )

    class Meta:
        model = SurfaceWaterStation
        fields = '__all__'
