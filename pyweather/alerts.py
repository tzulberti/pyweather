# -*- coding: utf-8 -*-


from pyweather.base import WundergroundAPI

class AlertsAPI(WundergroundAPI):
    ''' Returns the short name description, expiration time and a long text
    description of a severe alert, if one has been issued for the searched upon
    location.

    These alerts are only active in the United States and Europe. View our
    United States Severe Weather map or our European Severe Weather map to see
    where there are active alerts at this moment.

    Read the National Weather Service description of VTEC codes used in severe
    weather alerts in the United States, including "phenomena" and
    "significane", here: www.weather.gov/os/vtec/pdfs/VTEC_explanation6.pdf

    European alerts are required to show the "attribution" to Meteoalarm.

    An example of how to use this class:

    .. code-block:: python

        >>> import json
        >>> from pyweather.alerts import AlertsAPI
        >>> alerts = AlertsAPI('XXXXXXXX') # here goes the API code
        >>> data = alerts.using_country_and_city('IA', 'Des_Moines')
        >>> parsed_data = json.loads(data)

        >>> europe_alerts = AlertsAPI('XXXXXX')
        >>> europe_data = europe_alerts.using_personal_weather_station('zmw:00000.1.16172')
        >>> europe_data = json.loads(europe_data)


    The response for the cities within USA will have the following keys:

    * type
    * description
    * date
    * date_epoch
    * expires
    * expires_epoch
    * message
    * phenomena
    * significance
    * a list of ZONES which will have the following keys:

      - state
      - ZONE

    * a list of StormBased which will have the following keys:

      - Vertex_count
      - stormInfo
      - time_epoch
      - Motion_deg
      - Motion_spd
      - position_lat
      - position_lon
      - a list of vertices, which will have the following keys:

        * lat
        * lon

    The response for the cities within Europe will have the following keys:

    * type
    * wtype_meteoalarm
    * wtype_meteoalarm_name
    * level_meteoalarm
    * level_meteoalarm_name
    * level_meteoalarm_description
    * description
    * date
    * date_epoch
    * expires
    * expires_epochexpires_epoch
    * message
    * phenomena
    * significance
    * attribution


    More information about the response could be got from here `Weather
    Undergound Alerts API Documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/alerts>`_
    '''

    def __init__(self, api_key, **kwargs):
        super(Alerts, self).__init__(api_key=api_key,
                                     feature='alerts',
                                     **kwargs)
