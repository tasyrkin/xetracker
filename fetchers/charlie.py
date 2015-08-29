import urllib2
from lxml import etree
import logging
    
class CharlieFetcher:
  def fetch(self):
    str_catalog = urllib2.urlopen("http://charliescurrency.ca/rateswithcss.xml").read()
    return new CharlieTransformer(str_catalog)

class CharlieTransformer:
  def tranform(self, xml_string):
    catalog = etree.XML(xml_string)

    currency_conversions = list()
    for el in catalog:
      if (el.tag == 'TIMESTAMP'):
        timestamp = extract_timestamp(el.text)
      elif (el.tag == 'RATE'):
        currency_conversions.append(extract_conversion(el))
      else:
        logging.warning('{} tag is unknown'.format(el.tag))

    return currency_conversions
