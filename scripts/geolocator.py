# https://chrisalbon.com/python/data_wrangling/geolocate_a_city_or_country/
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myapp")
import numpy as np
import pandas as pd

def geolocate(city=None, country=None):
    '''
    Inputs city and country, or just country. Returns the lat/long coordinates of 
    either the city if possible, if not, then returns lat/long of the center of the country.
    '''
    
    # If the city exists,
    if city != None:
        # Try
        try:
            # To geolocate the city and country
            loc = geolocator.geocode(str(city + ',' + country))
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
    # If the city doesn't exist
    else:
        # Try
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude 
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan


'''
# Geolocate a city and country
geolocate(city='Austin', country='USA')

# Geolocate just a country
geolocate(country='USA')

'''
print(geolocate(city='Delhi', country='India'))


## read a csv file for column mapping

df = pd.read_csv('/home/superadmin/Downloads/territories.csv')
for index, row in df.iterrows() :
    # print(row['Country'], row['TerritoryDescription'])
    lat_lon = geolocate(city=row['Country'], country=row['TerritoryDescription'])
    print(lat_lon, type(lat_lon))
    if type(lat_lon) is tuple:
        (lat,lon) = lat_lon
        df['lat'] = lat
        df['lon'] = lon
    else :
        df['lat'] = np.nan
        df['lon'] = np.nan 
print(df)