# -*- coding: utf-8 -*-

from pyweather.base import WundergroundAPI

class ConditionsAPI(WundergroundAPI):
    ''' Returns the current temperature, weather condition, humidity, wind,
    'feels like' temperature, barometric pressure, and visibility.

    An example on how to use this class:

    .. code-block:: python

        >>> import json
        >>> from pyweather.conditions import ConditionsAPI
        >>> conditions = ConditionsAPI('XXXXXXXXX') # API key
        >>> data = conditions.using_state_and_city('CA', 'San Francisco')
        >>> print json.loads(data)

    The response will have the following keys:

    - image.url
    - image.title
    - image.link
    - display_location.full
    - display_location.city
    - display_location.state
    - display_location.state_name
    - display_location.country
    - display_location.country_iso3166
    - display_location.zip
    - display_location.latitude
    - display_location.longitude
    - display_location.elevation
    - observation_location.full
    - observation_location.city
    - observation_location.state
    - observation_location.country
    - observation_location.country_iso3
    - observation_location.latitude
    - observation_location.longitude
    - observation_location.elevation
    - estimated
    - station_id
    - observation_time
    - observation_time_rfc822
    - observation_epoch
    - local_time_rfc822
    - local_epoch
    - local_tz_short
    - local_tz_long
    - local_tz_offset
    - weather
    - temperature_string
    - temp_f
    - temp_c
    - relative_humidity
    - wind_string
    - wind_dir
    - wind_degrees
    - wind_mph
    - wind_gust_mph
    - wind_kph
    - wind_gust_kph
    - pressure_mb
    - pressure_in
    - pressure_trend
    - dewpoint_string
    - dewpoint_f
    - dewpoint_c
    - heat_index_string
    - heat_index_f
    - heat_index_c
    - windchill_string
    - windchill_f
    - windchill_c
    - feelslike_string
    - feelslike_f
    - feelslike_c
    - visibility_mi
    - visibility_km
    - solarradiation
    - UV
    - precip_1hr_string
    - precip_1hr_in
    - precip_1hr_metric
    - precip_today_string
    - precip_today_in
    - precip_today_metric
    - icon
    - icon_url
    - forecast_url
    - history_url
    - ob_url

    More information can be found at `Weather Underground Conditions API
    Documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/conditions>`_
    '''

    def __init__(self, api_key, **kwargs):
        super(ConditionsAPI, self).__init__(api_key=api_key,
                                            feature='conditions',
                                            **kwargs)
