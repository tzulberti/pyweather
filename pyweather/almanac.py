# -*- coding: utf-8 -*-


from pyweather.base import WundergroundAPI

class AlmanacAPI(WundergroundAPI):
    ''' Historical average temperature for today.

    The response will have the following keys:

    * airport_code
    * temp_high.normal.F
    * temp_high.normal.C
    * temp_high.record.F
    * temp_high.record.C
    * temp_high.recordyear
    * temp_low.normal.F
    * temp_low.normal.C
    * temp_low.record.F
    * temp_low.record.C
    * temp_low.recordyear

    An example on how to use it:

    .. code-block:: python

        >>> import json
        >>> from pyweather.almanac import AlmanacAPI
        >>> almanac = AlmanacAPI('XXXXXXX') # here goes the API KEY
        >>> data = almanac.using_state_and_city('CA', 'San Francisco')
        >>> print json.loads(data)

    More information can be found at `Weather Underground Almanac API
    documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/almanac>`_
    '''

    def __init__(self, api_key, **kwargs):
        super(AlmanacAPI, self).__init__(api_key=api_key,
                                         feature='almanac',
                                         **kwargs)
