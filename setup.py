import os

try:
  from setuptools import setup, Command
except:
  from distutils.core import setup, Command

class CleanCommand(Command):
  """Custom clean command to tidy up the project root."""
  user_options = []
  def initialize_options(self):
    pass
  def finalize_options(self):
    pass
  def run(self):
    os.system("rm -vrf ./build ./dist ./*.pyc ./*.tar.gz ./*.egg-info")

config = {
  "description": "Track the rates of the foreign currency traders",
  "author": "tasyrkin",
  "url": "https://github.com/tasyrkin/xetracker",
  "download_url": "https://github.com/tasyrkin/xetracker",
  "author_email": "tasyrkin@gmail.com",
  "version": "0.1",
  "install_requires": ["nose", "lxml", "urllib2", "psycopg2"],
  "packages": ["xetracker", "xetracker.model"],
  "scripts": [],
  "name": "xetracker",
  "cmdclass": {
    "clean": CleanCommand
  }
}

setup(**config)
