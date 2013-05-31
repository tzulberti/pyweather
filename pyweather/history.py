# -*- coding: utf-8 -*-

from pyweather.base import WundergroundAPI


class HistoryAPI(WundergroundAPI):
    ''' Returns a summary of the observed weather for the specified date.

    An example on how to use this classs:

    .. code-block:: python

        >>> import json
        >>> from datetime import date
        >>> from pyweather.history import HistoryAPI
        >>> history = HistoryAPI('XXXXXXX', date.today())
        >>> data = history.using_state_and_city('CA', 'San Francisco')
        >>> print json.loads(data)

    :param date date_for: the specified date for which the summary will be
                          returned.

    The response will have the following keys:

    - date
    - utcdate
    - observations: is a list, which have the following keys:

      * date
      * utcdate
      * tempm
      * tempi
      * dewptm
      * dewpti
      * hum
      * wspdm
      * wspdi
      * wgustm
      * wgusti
      * wdird
      * wdire
      * vism
      * visi
      * pressurem
      * pressurei
      * windchillm
      * windchilli
      * heatindexm
      * heatindexi
      * precipm
      * precipi
      * conds
      * icon
      * fog
      * rain
      * snow
      * hail
      * thunder
      * tornado
      * metar

    - dailysummary

        * date
        * fog
        * rain
        * snow
        * snowfallm
        * snowfalli
        * monthtodatesnowfallm
        * monthtodatesnowfalli
        * since1julsnowfallm
        * since1julsnowfalli
        * snowdepthm
        * snowdepthi
        * hail
        * thunder
        * tornado
        * meantempm
        * meantempi
        * meandewptm
        * meandewpti
        * meanpressurem
        * meanpressurei
        * meanwindspdm
        * meanwindspdi
        * meanwdire
        * meanwdird
        * meanvism
        * meanvisi
        * humidity
        * maxtempm
        * maxtempi
        * mintempm
        * mintempi
        * maxhumidity
        * minhumidity
        * maxdewptm
        * maxdewpti
        * mindewptm
        * mindewpti
        * maxpressurem
        * maxpressurei
        * minpressurem
        * minpressurei
        * maxwspdm
        * maxwspdi
        * minwspdm
        * minwspdi
        * maxvism
        * maxvisi
        * minvism
        * minvisi
        * gdegreedays
        * heatingdegreedays
        * coolingdegreedays
        * precipm
        * precipi
        * precipsource
        * heatingdegreedaysnormal
        * monthtodateheatingdegreedays
        * monthtodateheatingdegreedaysnormal
        * since1sepheatingdegreedays
        * since1sepheatingdegreedaysnormal
        * since1julheatingdegreedays
        * since1julheatingdegreedaysnormal
        * coolingdegreedaysnormal
        * monthtodatecoolingdegreedays
        * monthtodatecoolingdegreedaysnormal
        * since1sepcoolingdegreedays
        * since1sepcoolingdegreedaysnormal
        * since1jancoolingdegreedays
        * since1jancoolingdegreedaysnormal

    More information can be found at `Weather Underground History API
    Documentation
    <http://www.wunderground.com/weather/api/d/docs?d=data/history>`_
    '''

    def __init__(self, api_key, for_date, **kwargs):
        formated_date = for_date.strftime('%Y_%M')
        super(HistoryAPI, self).__init__(api_key=api_key,
                                         feature='history_%s' % formated_date,
                                         **kwargs)


