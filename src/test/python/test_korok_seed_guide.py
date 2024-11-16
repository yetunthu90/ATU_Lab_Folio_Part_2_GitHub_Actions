import unittest
from unittest.mock import patch
from io import StringIO
from src.main.python.korok_seed_guide import korok_seed_guide


class TestKorokSeedGuide(unittest.TestCase):
    @patch('builtins.input', side_effect=['10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_advanced_help(self, mock_stdout, mock_input):
        korok_seed_guide()
        self.assertIn("You have enough credits for advanced help!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_basic_hints(self, mock_stdout, mock_input):
        korok_seed_guide()
        self.assertIn("You can access basic hints!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_insufficient_credits(self, mock_stdout, mock_input):
        korok_seed_guide()
        self.assertIn("You need more credits to access help.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
