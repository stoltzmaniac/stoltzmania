from ast import literal_eval

from django.core.management.base import BaseCommand, CommandError
from stoltzmania.water.models import SurfaceWaterStation

import pandas as pd
import numpy as np


# Rename columns:
COLUMN_MAP = {
    'DIV': 'div',
    'WD': 'wd',
    'County': 'county',
    'State': 'state',
    'Station Name': 'station_name',
    'DWR Abbrev': 'dwr_abbrev',
    'USGS Station ID': 'usgs_station_id',
    'Data Source': 'data_source',
    'Status': 'status',
    'POR Start': 'por_start',
    'POR End': 'por_end',
    'UTM X': 'utm_x',
    'UTM Y': 'utm_y',
    'Location': 'location',
    'Location Accuracy': 'location_accuracy',
    'More Information': 'more_information'
}


class Command(BaseCommand):
    help = 'Truncates and ingests SWS data'

    def handle(self, *args, **options):
        try:
            SurfaceWaterStation.objects.all().delete()
            df = pd.read_csv('./stoltzmania/raw_data/water/DWR_Surface_Water_Stations.csv')
            df = df.replace(np.nan, None)
            df = df.rename(columns=COLUMN_MAP)
            sws = []
            for row in df.to_dict(orient='records'):
                if row.get('location') is not None:
                    pt = tuple(reversed(literal_eval(row['location'])))
                    pt_str = str(pt).replace(',', '')
                    row['geometry'] = f"POINT {pt_str}"
                sws_ = SurfaceWaterStation(**row)
                sws.append(sws_)            
            SurfaceWaterStation.objects.bulk_create(sws)
            self.stdout.write(self.style.SUCCESS('Created al SurfaceWaterStation objects from csv'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
            raise CommandError('Error during truncation, read data, insert SurfaceWaterStation ETL.')
