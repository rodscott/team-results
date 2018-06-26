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
    print({
        'MSEN': [
            {'club': 'A', 'counters': [('A1', 2), ('A2', 3), ('A3', 5)], 'score': 10},
            {'club': 'B', 'counters': [('B1', 1), ('B2', 4), ('B3', 6)], 'score': 11},
            {'club': 'C', 'counters': [('C1', 7), ('C2', 8), ('C3', 20)], 'score': 35}
        ],
        'WSEN': [
            {'club': 'A', 'counters': [('A1', 4), ('A2', 6), ('A3', 8)], 'score': 18},
            {'club': 'B', 'counters': [('B1', 3), ('B2', 11), ('B3', 15)], 'score': 29},
            {'club': 'C', 'counters': [('C1', 2), ('C2', 9), ('C3', 20)], 'score': 31}
        ]
    })


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
    with open(filename) as resultsfile:
        has_header = csv.Sniffer().has_header(resultsfile.read(1024))
        resultsfile.seek(0)
        reader = csv.DictReader(resultsfile, fieldnames=['position', 'name', 'category', 'club', 'time'], restkey='extra')
        if has_header:
            next(reader) # skip column names row 
        for result in reader:
            add_to_team(**result)


def add_to_team(position, name, category, club, time):
    pass

class Results:


    def __init__(self, filename):
        self.data = dict()


    def add(self, position, name, category, club, time):
        if category in self.data:
            pass
        else:
            self.data[club] = 


if __name__ == "__main__":
    main()
