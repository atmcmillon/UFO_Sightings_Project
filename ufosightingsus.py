"""UFO Sightings 
Austin McMillon"""

import pandas as pd
import numpy as np
import datetime as dt
import sweetviz as sv
import matplotlib as plt
#import geopandas as gp

ufodf = pd.read_csv('scrubbed.csv', index_col=0, low_memory=False)
ufodf = ufodf.reset_index()
ufodfinfo = ufodf.info
ufodfshape = ufodf.shape
#R: 80332, C: 10

"""ufo_report = sv.analyze(ufodf)
ufo_report.show_html('scrubbed.html')"""
#Undo lines 17 and 18 for the sweetviz data visualization file to view locally in a browser window


date_sighting = ufodf['datetime']

date_sighting = pd.to_datetime(ufodf['datetime'], errors='coerce')

date_logged = ufodf['date posted']

date_logged = pd.to_datetime(ufodf['date posted'], errors='coerce')

pd.to_datetime(date_logged)
city = ufodf['city'].str.capitalize()
state = ufodf['state'].str.upper()
country = ufodf['country'].str.upper()
shape = ufodf['shape'].str.capitalize()
#lat = ufodf['latitude']
#lon = ufodf['longitude']

uniqueco = country.unique()
uniquesh = shape.unique()
uniquest = state.unique()
