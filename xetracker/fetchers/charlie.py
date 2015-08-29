import sys
import logging
import datetime

import urllib2
from lxml import etree

from xetracker.model import currency_conversion 

class CharlieFetcher:
  def fetch(self):
    str_catalog = urllib2.urlopen("http://charliescurrency.ca/rateswithcss.xml").read()
    return CharlieTransformer().transform(str_catalog)

class CharlieTransformer:
  def transform(self, xml_string):
    catalog = etree.XML(xml_string)

    currency_conversions = list()
    timestamp_timestamp = None
    for el in catalog:
      if (el.tag == 'TIMESTAMP'):
        timestamp_datetime = self.__extract_timestamp(el)
      elif (el.tag == 'RATE'):
        currency_conversions.append(self.__extract_conversion(el, timestamp_datetime))
      else:
        logging.warning('{} tag is unknown'.format(el.tag))

    return currency_conversions

  def __extract_conversion(self, rate_element, timestamp_datetime):
    from_currency_str = self.__find_tag_value(rate_element, 'ISO')
    provider_selling_rate = self.__find_tag_value(rate_element, 'WESELL')
    provider_buying_rate = self.__find_tag_value(rate_element, 'WEBUY')
    return currency_conversion.CurrencyConversion('CHARLIE', from_currency_str, 'CAD', provider_selling_rate, provider_buying_rate, timestamp_datetime)

  def __find_tag_value(self, element, tag_name):
    for child_element in element:
      if child_element.tag == tag_name:
        return child_element.text
    return None

  def __extract_timestamp(self, timestamp_element):
    try:
      timestamp_str = timestamp_element.text
      timstamp_parts = timestamp_str.split(' ')
      return datetime.strptime('{} {} {}'.format(timestamp_parts[3], timestamp_parts[5], timestamp_parts[6]))
    except:
      e = sys.exc_info()[0]
      logging.error('Unable convert timestamp element: {}'.format(e))
      return datetime.datetime.now()
