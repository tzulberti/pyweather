# -*- coding: utf-8 -*-

from pyweather.base import WundergroundAPI


class Forecast10DaysAPI(WundergroundAPI):
    ''' Returns a summary of the weather for the next 3 days. This includes high
    and low temperatures, a string text forecast and the conditions.

    An example on how to use this class:

    .. code-block:: python

        >>> import json
        >>> from pyweather.forecast_10_days import Forecast10DaysAPI
        >>> forecast = Forecast10DaysAPI('XXXXXXX') # api key
        >>> data = forecast.using_state_and_city('CA', 'San Francisco')
        >>> print json.loads(data)

    The response will have the followin keys:

    - txt_forecast

      * forecastday: which will have a list of dict with the following keys:

        + period
        + icon
        + icon_url
        + title
        + fctext
        + fcttext_metric
        + pop

    - simpleforecast

      * forecastday: which will have a list with the following keys:

        + date
        + period
        + high
        + low
        + conditions
        + icon
        + icon_url
        + skyicon
        + pop
        + qpf_allday
        + qpf_day
        + qpf_night
        + snow_allday
        + snow_day
        + snow_night
        + maxwind
        + avewind
        + avehumidity
        + maxhumidity
        + minhumidity

    More information can be found at `Weather Underground Forecast API
    Documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/forecast>`_
    '''

    def __init__(self, api_key, **kwargs):
        super(ForecastAPI, self).__init__(api_key=api_key,
                                          feature='forecast10day',
                                          **kwargs)
