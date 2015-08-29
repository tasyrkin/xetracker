import urllib2
from lxml import etree
import logging

class CurrencyConvertion:
  def __init__(self, provider, currency_from, currency_to, rate, conversion_time):
    self.provider = provider
    self.currency_from = currency_from
    self.currency_to = currency_to
    self.rate = rate
    self.conversion_time = conversion_time

  def __str__(self):
    return 'CurrencyConversion[provider={}, currency_from={}, currency_to={}, rate={}, conversion_time={}]'.format(
        self.provider, self.currency_from, self_currency_to, self.rate, self.conversion_time)
    
def extract_conversions(element_catalog):
  currency_conversions = list()
  for el in catalog:
    if (el.tag == 'TIMESTAMP'):
      timestamp = extract_timestamp(el.text)
    elif (el.tag == 'RATE'):
      currency_conversions.append(extract_conversion(el))
    else:
      logging.warning('{} tag is unknown'.format(el.tag))
  return currency_conversions

def persist(currency_conversions):
  #save them to db

str_catalog = urllib2.urlopen("http://charliescurrency.ca/rateswithcss.xml").read()

catalog = etree.XML(str_catalog)

currency_conversions = extract_conversions(catalog)

persist(currency_conversions)
