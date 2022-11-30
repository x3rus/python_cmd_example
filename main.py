#!/usr/bin/python
#

from configparser import ConfigParser
import mySuperApp
import mySuperAppConfig


#config_parser = ConfigParser()
#config_parser.read('toto.ini')


#print(config_parser['camunda']['base_url'])

def process_args():
    # So here it will be cmd or env variable
    a_dict = {}
    a_dict['conf_filename']='toto.ini'
    return a_dict


if __name__ == "__main__":
    # in reality I have this 
    cmd_args = process_args()
    config_for_my_app = mySuperAppConfig.mySuperAppConfig(cmd_args['conf_filename']) 
    app = mySuperApp.mySuperApp(config_for_my_app.get_settings())
    app.run_or_app_action()

