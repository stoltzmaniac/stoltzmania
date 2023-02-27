from django.urls import path

import stoltzmania.water.views as views

app_name = "water"
urlpatterns = [
    path("", view=views.SurfaceWaterStationFormView.as_view(), name="surface_water_station")
]
