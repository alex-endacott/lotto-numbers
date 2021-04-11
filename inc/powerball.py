"""
All the logic for analysing winning Powerball numbers
"""


import pandas as pd

PB_PRIOR_WINNERS_DATA_PATH = 'prior_winners/powerball.csv'


def get_prior_pb_winners_data():
    """
    Reads in Powerball csv data
    :return:
    """
    pb_df = pd.read_csv(PB_PRIOR_WINNERS_DATA_PATH)
    pb_df.columns = ['num1', 'num2', 'num3', 'num4', 'num5', 'pb']
    print(pb_df.iloc[0])
