from unittest.mock import patch
import results


def test_default_commandline_arguments():
    with patch('sys.argv', ['prog', '-f', 'results.csv']):
        assert ('results.csv', 'MSEN', 3) == results.capture_commandline_args()


def test_non_default_using_short_commandline_arguments():
    with patch('sys.argv', ['prog', '-f', 'race-results.csv', '-c', 'W40', '-t', '4']):
        assert ('race-results.csv', 'W40', 4) == results.capture_commandline_args()


def test_non_default_using_long_commandline_arguments():
    with patch('sys.argv', ['prog','--filename', 'race.csv', '--category', 'M60', '--team-size', '8']):
        assert ('race.csv', 'M60', 8) == results.capture_commandline_args()


def test_read_results_csv_file():   
    assert 14 == len(results.read_results_csv_file('fixtures/results.csv'))
