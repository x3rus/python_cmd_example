#!/usr/bin/python
#

from configparser import ConfigParser
import mySuperApp


#config_parser = ConfigParser()
#config_parser.read('toto.ini')


#print(config_parser['camunda']['base_url'])



if __name__ == "__main__":
    app = mySuperApp.mySuperApp(None)
    app.run_or_app_action()

