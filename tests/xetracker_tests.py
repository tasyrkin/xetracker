from nose.tools import *
from xetracker.fetchers import charlie

def setup():
  pass

def teardown():
  pass

def test_transform_timestamp_and_rates():
  xml_str = open('tests/resources/timestamp_and_two_rates.xml', 'r').read()
  transformer = charlie.CharlieTransformer()
  conversions = transformer.transform(xml_str)
  assert_equal(2, len(conversions))
