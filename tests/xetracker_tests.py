import datetime
from nose.tools import *

from xetracker.fetchers import charlie
from xetracker.model import currency_conversion

def setup():
  pass

def teardown():
  pass

def test_transform_timestamp_and_rates():
  xml_str = open('tests/resources/timestamp_and_two_rates.xml', 'r').read()
  conversions = charlie.CharlieTransformer().transform(xml_str)

  assert_equal(2, len(conversions))
  expected_usd2cad = currency_conversion.CurrencyConversion('CHARLIE', 'USD', 'CAD', '1.327', '1.3098', datetime.datetime.strptime('8/29/2015 06:03:56', '%m/%d/%Y %H:%M:%S'))
  assert_equal(conversions[0], expected_usd2cad)

  expected_aud2cad = currency_conversion.CurrencyConversion('CHARLIE', 'AUD', 'CAD', '0.9555', '0.9308', datetime.datetime.strptime('8/29/2015 06:03:56', '%m/%d/%Y %H:%M:%S'))
  assert_equal(conversions[1], expected_aud2cad)
