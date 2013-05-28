# -*- coding: utf-8 -*-

from pyweather.base import WundergroundAPI


class CurrentHurricaneAPI(WundergroundAPI):
    ''' Returns information about current hurricanes and tropical storms.

    This feature can be used with other weather API features. However, location
    query options do not apply to the results for currenthurricane.

    The response will have the following fields:

    - stormInfo

      * stormName
      * stormName_Nice
      * stormNumber

    - current

      * lat
      * lon
      * SaffirSimpsonCategory
      * Category
      * Time
      * TimeGMT
      * WindSpeed
      * WindGust
      * Fspeed
      * Forward speed of the storm
      * Movement

        + Degrees
        + Text

      * Pressure

        + mb
        + inches

      * WindQuadrants
      * WindRadius
      * SeaQuadrants
      * SeaRadius

    - forecast (it has the same fields as current, but it add the following
      keys):

      * ForecastHour

    - ExtendedForecast
    - trac

    More information can be found at `Weather Underground Current Huricane API
    Documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/currenthurricane>`_
    '''

    def __init__(self, api_key, **kwargs):
        super(CurrentHurricaneAPI, self).__init__(api_key=api_key,
                                                  feature='currenthurricane',
                                                  **kwargs)
