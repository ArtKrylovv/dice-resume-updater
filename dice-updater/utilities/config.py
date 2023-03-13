import yaml
from yaml.loader import SafeLoader


def get_data():
    """
    This function returns data from config.yaml file.
    """
    with open('./config.yaml') as config:
        data = yaml.load(config, Loader=SafeLoader)
    return data
