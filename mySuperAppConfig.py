from configparser import ConfigParser
from pydantic import (
    BaseSettings
)

class Settings(BaseSettings):
    base_url : str


class mySuperAppConfig:
    """ My will safe the word """
    def __init__(self, config_filename):
        """ Initialisation of the class

        param : config_filename : file path where the ini file is 
        """
        self.config_parser = ConfigParser()
        # Personnaly when I create a class I do not process too much things 
        # in the init so I use another function to initiate the process 
        # here it will be load_config()
        # self.config_parser.read(config_filename)
        self.config_filename = config_filename

        # Optional if you want to keep the processed information in memory
        # but it will already be loaded in the memory of the end app
        # self.settings = None

    def reload_config_in_memory(self):
        pass

    def get_settings(self):
#        if we have it ... no need to process :) 
#        if self.settings is not None:
#            return self.settings
        self.config_parser.read(self.config_filename)

        # Of course more CODE regarding the data validation process execption throw ... 
        local_settings = Settings(base_url=self.config_parser['camunda']['base_url'])

        return local_settings

