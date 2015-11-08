import sys
import logging
import datetime
from decimal import *

import urllib2
from lxml import etree

from xetracker.model import currency_conversion 

class CharlieFetcher:
  def fetch(self):
    str_catalog = urllib2.urlopen("http://charliescurrency.ca/rateswithcss.xml").read()
    return CharlieTransformer().transform(str_catalog)

class CharlieTransformer:

  TIMESTAMP_TAG = 'TIMESTAMP'
  RATE_TAG = 'RATE'
  ISO_TAG = 'ISO'
  WESELL_TAG = 'WESELL'
  WEBUY_TAG = 'WEBUY'
  CHARLIE_PROVIDER = 'CHARLIE'
  CAD = 'CAD'

  def transform(self, xml_string):
    catalog = etree.XML(xml_string)

    currency_conversions = list()
    timestamp_timestamp = None
    for el in catalog:
      if (el.tag == self.TIMESTAMP_TAG):
        timestamp_datetime = self.__extract_timestamp(el)
      elif (el.tag == self.RATE_TAG):
        currency_conversions.append(self.__extract_conversion(el, timestamp_datetime))
      else:
        logging.warning('{} tag is unknown'.format(el.tag))

    return currency_conversions

  def __extract_conversion(self, rate_element, timestamp_datetime):
    from_currency_str = self.__find_tag_value(rate_element, self.ISO_TAG)
    provider_selling_rate = self.__find_tag_value(rate_element, self.WESELL_TAG)
    provider_buying_rate = self.__find_tag_value(rate_element, self.WEBUY_TAG)
    return currency_conversion.CurrencyConversion(
        self.CHARLIE_PROVIDER,
        from_currency_str,
        self.CAD,
        Decimal(provider_selling_rate),
        Decimal(provider_buying_rate),
        timestamp_datetime)

  def __find_tag_value(self, element, tag_name):
    for child_element in element:
      if child_element.tag == tag_name:
        return child_element.text
    return None

  def __extract_timestamp(self, timestamp_element):
    try:
      # Incoming string is 'Rates updated on 11/07/15 at 23:46:50 PST'
      # therefore date is on idx=3, time is on idx=5
      timestamp_parts = timestamp_element.text.split(' ')
      date = timestamp_parts[3]
      time = timestamp_parts[5]
      date_time = '{} {}'.format(date, time)

      time_format = '%H:%M:%S'

      try:
        return datetime.datetime.strptime(date_time, '%m/%d/%Y {}'.format(time_format))
      except:
        return datetime.datetime.strptime(date_time, '%m/%d/%y {}'.format(time_format))
    except:
      e = sys.exc_info()[0]
      logging.error('Unable convert timestamp element: {}, {}'.format(e, timestamp_element.text))
      return datetime.datetime.now()
