from argparse import ArgumentParser
from lib.change_combos import ChangeCombos


COIN_TYPES = [1, 5, 10, 25, 50, 100]


def main():
    parser = ArgumentParser(usage="usage: change_combos.py <target> [-h] [--coins COINS [COINS ...]]",
                            description='Find number of change combinations \
                                         for given dollar value in cents.')

    parser.add_argument('target', metavar='target', type=int,
                        help='Target dollar value in cents - ex $1.50 = 150')

    parser.add_argument('--coins', dest='coins', type=int, nargs='+', required=False,
                        default=COIN_TYPES,
                        help='Array of possible coins.')

    parser._add_container_actions

    args = parser.parse_args()

    change_combos = ChangeCombos(args.coins)

    print 'Change Combinations: {0}'.format(change_combos.combo_count(args.target))

    return 0

if __name__ == "__main__":
    main()
