#!/usr/bin/python
#

from configparser import ConfigParser


config_parser = ConfigParser()
config_parser.read('toto.ini')


print(config_parser['camunda']['base_url'])

