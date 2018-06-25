from unittest.mock import patch
import results


def test_default_commandline_arguments():
    with patch('sys.argv', ['prog']):
        assert ('MSEN', 3) == results.capture_commandline_args()


def test_non_default_using_short_commandline_arguments():
    with patch('sys.argv', ['prog', '-c', 'W40', '-t', '4']):
        assert ('W40', 4) == results.capture_commandline_args()


def test_non_default_using_long_commandline_arguments():
    with patch('sys.argv', ['prog', '--category', 'M60', '--team-size', '8']):
        assert ('M60', 8) == results.capture_commandline_args()
