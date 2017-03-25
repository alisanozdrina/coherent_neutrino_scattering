import logging
import configparser

#---------------------------------------------------------------------------
# Load config file to dictionary `config`
#---------------------------------------------------------------------------
config = {}


def _load_config():
    config_file = configparser.ConfigParser()
    config_file.read('./config.ini')
    global config
    for key in config_file['default']:
        config[key.upper()] = config_file['default'][key]

_load_config()

#---------------------------------------------------------------------------
# Logger configuration
#---------------------------------------------------------------------------
logging.basicConfig(level=config['LOG_LEVEL'], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')
