"""
All the logic for analysing winning Powerball numbers
"""


import pandas as pd
import numpy as np

PB_PRIOR_WINNERS_DATA_PATH = 'prior_winners/powerball.csv'
PB_PRIOR_WINNERS_COLUMNS = ['num1', 'num2', 'num3', 'num4', 'num5', 'pb']
COLUMNS_TO_SORT = ['num1', 'num2', 'num3', 'num4', 'num5']


def import_prior_pb_winners_csv() -> pd.DataFrame:
    """
    Reads in Powerball csv data
    :return: A DataFrame with the Powerball csv data
    """
    pb_df = pd.read_csv(PB_PRIOR_WINNERS_DATA_PATH, header=None)
    return pb_df


def format_prior_pb_winners_data(pb_df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats Powerball data into ascending values on each row
    :param pb_df: An unformatted DataFrame
    :return: A formatted DataFrame
    """
    pb_df.columns = PB_PRIOR_WINNERS_COLUMNS
    pb_df[COLUMNS_TO_SORT] = np.sort(pb_df[COLUMNS_TO_SORT].values)
    return pb_df
