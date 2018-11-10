# https://chrisalbon.com/python/data_wrangling/geolocate_a_city_or_country/
# https://realpython.com/fast-flexible-pandas/
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
'''
for index, row in df.iterrows() :
    # print(row['Country'], row['TerritoryDescription'])
    lat_lon = geolocate(city=row['Country'], country=row['TerritoryDescription'])
    print(lat_lon, type(lat_lon))
    lat_list = []
    lon_list = []
    if type(lat_lon) is tuple:
        (lat,lon) = lat_lon
        lat_list.append(lat)
        lon_list.append(lon)
    else :
        lat_list.append(np.nan)
        lat_list.append(np.nan) 
    df['lat'] = lat_list
    df['lon'] = lon_list
print(df)
df.to_csv('lat_lon.csv')
'''
def get_geocode(country, city):
    """retruns the lat long of the given country and city."""    

    lat_lon = geolocate(country=country, city=city)
    if type(lat_lon) is tuple:
        (lat,lon) = lat_lon
        
    else :
        lat = np.nan
        lon = np.nan 
    return lat,lon

def append_lat_lon_withapply(df):
    df['lat_lon'] = df.apply(
        lambda row: get_geocode(
            country=row['Country'],
            city = row['TerritoryDescription']),
        axis=1)
    print(df)

append_lat_lon_withapply(df)
df

df['A'], df['B'] = df['lat_lon'].str.split(',', 1).str

df['A'] = df['A'].str.replace('(','')
df['B'] = df['B'].str.replace(')','')
df
df = df.to_csv('/home/superadmin/Downloads/territories_01.csv')
