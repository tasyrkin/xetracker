import datetime
from decimal import *
from nose.tools import *

from xetracker.fetchers import charlie
from xetracker.model import currency_conversion
from xetracker.persistance import currency_conversion_dao

def setup():
  pass

def teardown():
  pass

def test_transform_timestamp_and_rates_charlie():
  xml_str = open('tests/resources/timestamp_and_two_rates.xml', 'r').read()
  conversions = charlie.CharlieTransformer().transform(xml_str)

  assert_equal(2, len(conversions))
  expected_usd2cad = currency_conversion.CurrencyConversion('CHARLIE', 'USD', 'CAD', Decimal('1.327'), Decimal('1.3098'), datetime.datetime.strptime('8/29/2015 06:03:56', '%m/%d/%Y %H:%M:%S'))
  assert_equal(conversions[0], expected_usd2cad)

  expected_aud2cad = currency_conversion.CurrencyConversion('CHARLIE', 'AUD', 'CAD', Decimal('0.9555'), Decimal('0.9308'), datetime.datetime.strptime('8/29/2015 06:03:56', '%m/%d/%Y %H:%M:%S'))
  assert_equal(conversions[1], expected_aud2cad)

def test_persistance():
  dao = currency_conversion_dao.CurrencyConversionDAO()
  eur2cad = currency_conversion.CurrencyConversion('CHARLIE', 'EUR', 'CAD', Decimal('1.33'), Decimal('1.55'), datetime.datetime.now())
  
  dao.upsert([eur2cad])
  
  actual_eur2cad = dao.get(eur2cad.provider, eur2cad.currency_from, eur2cad.currency_to, eur2cad.conversion_time)

  assert_equal(actual_eur2cad, eur2cad)
