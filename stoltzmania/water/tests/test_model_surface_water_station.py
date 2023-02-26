import pytest

from stoltzmania.water.models import SurfaceWaterStation


SURFACE_WATER_STATION = {
    'div': 10,
    'wd': 11,
    'county': 'Larimer',
    'state': 'CO',
    'station_name': 'Stoltz Station',
    'dwr_abbrev': 'STST',
    'usgs_station_id': 12345,
    'data_source': 'USER',
    'status': 'Active',
    'por_start': 2023,
    'por_end': 2023,
    'utm_x': 44444,
    'utm_y': 55555,
    'location': 'User Supplied',
    'geometry': 'POINT(-105.0844 40.5853)'
}


@pytest.mark.django_db
def test_surface_water_station_model_creation():
    """Tests to ensure model accepts all inputs"""
    
    # No surface water stations should exist
    sws_expected_0 = SurfaceWaterStation.objects.all()
    assert len(sws_expected_0) == 0

    sws = SurfaceWaterStation(**SURFACE_WATER_STATION)
    sws.save()

    assert len(SurfaceWaterStation.objects.all()) == 1

    
