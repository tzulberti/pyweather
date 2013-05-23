# -*- coding: utf-8 -*-

from pyweather.base import WundergroundAPI


class AstronomyAPI(WundergroundAPI):
    ''' Returns the moon phase, sunrise and sunset times.

    The response will have the following keys:

    * precentIlluminated
    * ageOfMoon
    * current_time.hour
    * current_time.minute
    * sunrise.hour
    * sunrise.minute
    * sunset.hour
    * sunset.minute

    An example:

    .. code-block:: python

        >>> import json
        >>> from pyweather.astronomy import AstronomyAPI
        >>> astronomy = AstronomyAPI('XXXXXXX') # here goes the API key
        >>> data = astronomy.using_country_and_city('Argentina', 'Buenos Aires')
        >>> print json.loads(data)


    More information about this could be found at `Weather Underground Astronomy
    API Documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/astronomy>`_
    '''

    def __init__(self, api_key, **kwargs):
        super(AstronomyAPI, self).__init__(api_key=api_key,
                                           features='astronomy',
                                           **kwargs)
