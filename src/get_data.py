## read params
## process
## return dataframe
from distutils.command.config import config
import os
#import yaml
#import pandas as pd
import argparse
import pandas as pd
import yaml


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config= read_params(config_path)
    print(config)
    #data_path = config[]



if __name__=="__main":
    args= argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)