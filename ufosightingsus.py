"""UFO Sightings 
Austin McMillon"""

import pandas as pd
import numpy as np
import datetime as dt
import sweetviz as sv
#import geopandas as gp

ufodf = pd.read_csv('scrubbed.csv', index_col=0, low_memory=False, parse_dates=True)
ufodf = ufodf.reset_index()
ufodfinfo = ufodf.info
ufodfshape = ufodf.shape
#R: 80332, C: 10

"""ufo_report = sv.analyze(ufodf)
ufo_report.show_html('scrubbed.html')"""

#ufodf['datetime'] = ufodf['datetime'].dt.strftime('%d-%m-%Y %H:%M')
#Why are you being difficult about converting to dt?
date_sighting = ufodf['datetime']
date_logged = ufodf['date posted']
city = ufodf['city'].str.capitalize()
state = ufodf['state'].str.upper()
country = ufodf['country'].str.upper()
shape = ufodf['shape'].str.capitalize()
#lat = ufodf['latitude']
#lon = ufodf['longitude']

"""uniqueco = country.unique()
uniquesh = shape.unique()

print(uniquesh)"""
