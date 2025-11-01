import os
from configparser import ConfigParser

def read_configurations(category, key):
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini')
    config.read(os.path.abspath(config_path))
    return config.get(category, key)

