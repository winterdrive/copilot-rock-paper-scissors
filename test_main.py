import unittest
from unittest.mock import patch
from main import play_game

class TestGame(unittest.TestCase):
    @patch('builtins.input', return_value='rock')
    def test_user_chooses_rock(self, mock_input):
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_called_with("It's a tie!")

    @patch('builtins.input', return_value='paper')
    def test_user_chooses_paper(self, mock_input):
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_called_with("Computer wins!")

    @patch('builtins.input', return_value='scissors')
    def test_user_chooses_scissors(self, mock_input):
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_called_with("You win!")

    @patch('builtins.input', return_value='invalid')
    def test_user_chooses_invalid_choice(self, mock_input):
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_called_with("Invalid choice. Please try again.")

if __name__ == '__main__':
    unittest.main()