"""
A program to generate lotto-numbers numbers for the Mega Millions
and Powerball lotteries using patterns recognized from
previous winning numbers.
"""

import inc.powerball as pb


def main():
    pb.get_prior_pb_winners_data()


if __name__ == '__main__':
    main()
