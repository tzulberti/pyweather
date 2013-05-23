# -*- coding: utf-8 -*-

from requests import get


BASE_URL = 'http://api.wunderground.com/api/{api_key}/{feature}/lang:{language}/q/{query}.{format}'


class WundergroundAPI(object):
    ''' The class that maps the API to get the data.

    :param string api_key: the API key that will be used to get the
                           response from wunderground.com.

    :param string feature: the feature that you want to request to
                           wunderground.com. Some valid examples are:
                           forecast, conditions, geolookup, etc...

    :param string format: the format of the response. By default is json
    :param string base_url: the base URL that will be used to get the
                            data. It is URL that will be formated
                            with the API key, feature, and query.
    :param string language: the language in which the information will be
                            returned. By default is EN.
    '''

    def __init__(self, api_key, feature, format='.json', base_url=BASE_URL,
                 language='EN'):
        self.base_url = base_url
        self.api_key = api_key
        self.feature = feature
        self.format = format
        self.language = language

    def _get_response(self, query_url, query_data=dict()):
        url_data = dict(api_key=self.api_key,
                        format=self.format,
                        feature=self.feature,
                        language=self.language,
                        query=query_url)
        final_url = self.base_url.format(**url_data)
        if query_data:
            final_url = final_url.format(**query_data)
        wunderground_response = get(final_url)
        return wunderground_response.content

    def using_state_and_city(self, state_code, city):
        ''' Gets the information using the state and city.

        This seems to work only for USA states.

        :param str state_code: the two letters state name. For example, 'CA'
        :param str city: the whole name of the city. For example: 'San
                         Francisco'
        '''
        data = dict(state_code=state_code, city=city)
        return self._get_response('{state_code}/{city}', data)


    def using_country_and_city(self, country, city):
        ''' Gets the geolocation for the country and city.

        For example::

        .. code-block:: python

            >>> using_country_and_city('Argentina', 'Buenos Aires')
            {......}

        :param string api_key: the wunderground API.
        :para string country: the country name
        :param string city: the city name.

        :return: all the data returned by wunderground (as a string)
        '''
        data = dict(country=country, city=city)
        return self._get_response('{country}/{city}', data)

    def using_autoip(self):
        ''' Return the information based on the IP from where the
        request is done.

        .. code-block:: python

            >>> using_autoip()
            {....}

        :return: all the data returned by wunderground (as a string)
        '''
        return self._get_response('autoip')

    def using_postal_code(self, postal_code):
        ''' Get the information based on a postal code or ZIP.

        .. code-block:: python

            >>> using_postal_code('94107')

        :return: all the data returned by wunderground (as a string)
        '''
        data = dict(postal_code=postal_code)
        return self._get_response('{postal_code}', data)

    def using_airport_code(self, airport_code):
        ''' Gets the information using the airport code.

        .. code-block:: python
        '''
        data = dict(airport_code=airport_code)
        return self._get_response('{airport}', data)

    def using_latitud_and_longitud(self, latitud, longitud):
        '''
        '''
        data = dict(latitud=str(latitud), longitud=str(longitud))
        return self._get_response('{latitud},{longitud}', data)

    def using_personal_weather_station(self, weather_station):
        '''
        '''
        data = dict(weather_station=weather_station)
        return self._get_response('{weather_station}', data)
