import argparse
import csv
import sys


def main():
    check_python3()
    filename, category, team_size = capture_commandline_args()
    print(
        'Filename: {filename}, Category: {category}, Team size: {team_size}'
        .format(filename=filename, category=category, team_size=team_size)
    )
    print(read_results_csv_file('fixtures/results.csv'))
    print({'MSEN': [
        {'club': 'A', 'counters': [('A1', 2), ('A2', 3), ('A3', 5)], 'score': 10},
        {'club': 'B', 'counters': [('B1', 1), ('B2', 4), ('B3', 6)], 'score': 11}
    ]})


def check_python3():
    if sys.version_info[0] < 3 and sys.version_info[1] < 6:
        exit('ERROR: Python 3.6 or greater required')


def capture_commandline_args():
    parser = argparse.ArgumentParser(description='Calculate team results for a fell race')
    parser.add_argument('-f', '--filename', help='Results filename in csv format. Expected columns: position, name, category, club, time')
    parser.add_argument('-c', '--category', help='Category of team', default='MSEN')
    parser.add_argument('-t', '--team-size', type=int, help='Size of team', default=3)

    args = parser.parse_args()
    return args.filename, args.category, args.team_size


def read_results_csv_file(filename):
    to_return = []
    with open(filename) as resultsfile:
        has_header = csv.Sniffer().has_header(resultsfile.read(1024))
        resultsfile.seek(0)
        reader = csv.DictReader(resultsfile, fieldnames=['position', 'name', 'category', 'club', 'time'], restkey='extra')
        if has_header:
            next(reader) # skip column names row 
        for row in reader:
            to_return.append(row)
    return to_return


def get_teams(team_size, category):
    []


if __name__ == "__main__":
    main()
