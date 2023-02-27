from django.shortcuts import render
from django.views.generic.edit import FormView
from stoltzmania.water.forms import SurfaceWaterStationForm


class SurfaceWaterStationFormView(FormView):
    template_name = 'water/new_surface_water_station.html'
    form_class = SurfaceWaterStationForm
    success_url = ''
