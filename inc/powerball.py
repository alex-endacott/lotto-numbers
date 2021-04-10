"""
All the logic for analysing winning Powerball numbers
"""


import pandas as pd

PB_DATA_PATH = 'prior_winners/powerball.csv'


def get_prior_pb_winners_data():
    """
    Reads in Powerball csv data
    :return:
    """
    pd.read_csv(PB_DATA_PATH)
