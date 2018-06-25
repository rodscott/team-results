import sys
import argparse


def main():
    check_python3()
    category, team_size = capture_commandline_args()
    print('Category: {category}, Team size: {team_size}'.format(category=category, team_size=team_size))


def check_python3():
    if sys.version_info[0] < 3:
        exit('ERROR: Python 3 or greater required')


def capture_commandline_args():
    parser = argparse.ArgumentParser(description='Calculate team results for a fell race')
    parser.add_argument('-c', '--category', help='category of team', default='MSEN')
    parser.add_argument('-t', '--team-size', type=int, help='size of team', default=3)

    args = parser.parse_args()
    return args.category, args.team_size


if __name__ == "__main__":
    main()