"""
A program to generate lotto numbers for the Mega Millions
and Powerball lotteries using patterns recognized from
previous winning numbers.

PowerBall data collected from:
https://www.txlottery.org/export/sites/lottery/Games/Powerball/Winning_Numbers/

Mega Millions data collected from:
https://www.txlottery.org/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/
"""

import inc.powerball as pb


def main():
    pb_df = pb.import_prior_pb_winners_csv()
    formatted_pb_df = pb.format_prior_pb_winners_data(pb_df)


if __name__ == '__main__':
    main()
