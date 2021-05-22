"""
A program to generate lotto numbers for the Mega Millions
and Powerball lotteries using patterns recognized from
previous winning numbers.
"""

import inc.powerball as pb


def main():
    pb_df = pb.import_prior_pb_winners_csv()
    formatted_pb_df = pb.format_prior_pb_winners_data(pb_df)


if __name__ == '__main__':
    main()
