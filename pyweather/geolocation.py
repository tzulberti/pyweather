# -*- coding: utf-8 -*-

'''
'''

from pyweather.base import WundergroundAPI


class Geolookup(WundergroundAPI):
    '''
    Returns the city name, zip code / postal code, latitude-longitude
    coordinates and nearby personal weather stations.

    The response will have the following keys:

    - type
    - country
    - country_iso3166
    - country_name
    - state
    - city
    - tz_short
    - tz_long
    - lat
    - lon
    - zip
    - magic
    - wmo
    - l
    - requesturl
    - wuiurl
    - a lista of nearby weather stations. Which will have the following
      keys:

      * country
      * icao
      * lat
      * lon
      * state
      * city
    '''

    def __init__(self, api_key, **kwargs):
        super(Geolookup, self).__init__(api_key=api_key,
                                        feature='geolookup',
                                        **kwargs)

