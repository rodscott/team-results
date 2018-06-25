import unittest
from unittest.mock import patch
import results

class ResultsTestCases(unittest.TestCase):


    def test_default_commandline_arguments(self):
        test_args = ['prog']
        with patch('sys.argv', test_args):
            category, team_size = results.capture_commandline_args()
            self.assertEqual((category, team_size), ('MSEN', 3), 'Should be default values')


    def test_non_default_using_short_commandline_arguments(self):
        test_args = ['prog', '-c', 'W40', '-t', '4']
        with patch('sys.argv', test_args):
            category, team_size = results.capture_commandline_args()
            self.assertEqual((category, team_size), ('W40', 4), 'Should be specified values')


    def test_non_default_using_long_commandline_arguments(self):
        test_args = ['prog', '--category', 'M60', '--team-size', '8']
        with patch('sys.argv', test_args):
            category, team_size = results.capture_commandline_args()
            self.assertEqual((category, team_size), ('M60', 8), 'Should be specified values')


if __name__ == '__main__':
    unittest.main()