import argparse
import csv
from operator import itemgetter
import sys


def main():
    check_python3()
    filename, category, team_size = capture_commandline_args()
    results = Results()
    read_results_csv_file(filename, results)
    results.calculate(category, team_size)
    print(results.data)
    # print({
    #     'MSEN': [
    #         {'club': 'A', 'counters': [('A1', 2), ('A2', 3), ('A3', 5)], 'score': 10},
    #         {'club': 'B', 'counters': [('B1', 1), ('B2', 4), ('B3', 6)], 'score': 11},
    #         {'club': 'C', 'counters': [('C1', 7), ('C2', 8), ('C3', 20)], 'score': 35}
    #     ],
    #     'WSEN': [
    #         {'club': 'A', 'counters': [('A1', 4), ('A2', 6), ('A3', 8)], 'score': 18},
    #         {'club': 'B', 'counters': [('B1', 3), ('B2', 11), ('B3', 15)], 'score': 29},
    #         {'club': 'C', 'counters': [('C1', 2), ('C2', 9), ('C3', 20)], 'score': 31}
    #     ]
    # })


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


def read_results_csv_file(filename, results):
    with open(filename, newline='') as f:
        has_header = csv.Sniffer().has_header(f.read(1024))
        f.seek(0)
        reader = csv.reader(f)
        if has_header:
            next(reader) # skip column names row 
        for row in reader:
            results.add(row[0], row[1], row[2], row[3], row[4])


class Results:

    def __init__(self):
        self.data = {}

    def _process_club(self, club, gender, age, team_size):
        team = self.data[club]['team']
        category_team = []
        [category_team.append(runner) for runner in team if runner['gender'] == gender and runner['age'] >= age]
        category_team.sort(key=itemgetter('position'))
        self.data[club]['team'] = category_team[0:team_size]
        if len(category_team) >= team_size:
            self.data[club]['eligible'] = True
        else:
           self.data[club]['eligible'] = False

    def _age(self, category):
        if category in ['MSEN', 'WSEN']:
            return 18
        else:
            return int(category[1:])

    def _gender(self, category):
        return category[0]

    def add(self, position, name, category, club, time):
        if club not in self.data:
            self.data[club] = {'team': []}
        
        self.data[club]['team'].append({'position': int(position), 'name': name, 'age': self._age(category), 'gender': self._gender(category)})

    def calculate(self, category, team_size):
        [self._process_club(club, self._gender(category), self._age(category), team_size) for club in self.data]


if __name__ == "__main__":
    main()
