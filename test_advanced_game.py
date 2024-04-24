import unittest
from unittest.mock import patch
from advanced_game import determine_winner

class TestGame(unittest.TestCase):
    @patch('builtins.print')
    def test_paper_vs_rock(self, mock_print):
        result = determine_winner("paper", "rock")
        self.assertEqual(result, "You win!")


    @patch('builtins.print')
    def test_paper_vs_paper(self, mock_print):
        result = determine_winner("paper", "paper")
        self.assertEqual(result, "It's a tie!")


    @patch('builtins.print')
    def test_paper_vs_scissors(self, mock_print):
        result = determine_winner("paper", "scissors")
        self.assertEqual(result, "Computer wins!")


    @patch('builtins.print')
    def test_paper_vs_lizard(self, mock_print):
        result = determine_winner("paper", "lizard")
        self.assertEqual(result, "Computer wins!")


    @patch('builtins.print')
    def test_paper_vs_spock(self, mock_print):
        result = determine_winner("paper", "spock")
        self.assertEqual(result, "You win!")


    @patch('builtins.print')
    def test_scissors_vs_rock(self, mock_print):
        result = determine_winner("scissors", "rock")
        self.assertEqual(result, "Computer wins!")

    @patch('builtins.print')
    def test_scissors_vs_paper(self, mock_print):
        result = determine_winner("scissors", "paper")
        self.assertEqual(result, "You win!")

    @patch('builtins.print')
    def test_scissors_vs_scissors(self, mock_print):
        result = determine_winner("scissors", "scissors")
        self.assertEqual(result, "It's a tie!")

    @patch('builtins.print')
    def test_scissors_vs_lizard(self, mock_print):
        result = determine_winner("scissors", "lizard")
        self.assertEqual(result, "You win!")

    @patch('builtins.print')
    def test_scissors_vs_spock(self, mock_print):
        result = determine_winner("scissors", "spock")
        self.assertEqual(result, "Computer wins!")

    @patch('builtins.print')
    def test_lizard_vs_rock(self, mock_print):
        result = determine_winner("lizard", "rock")
        self.assertEqual(result, "Computer wins!")

    @patch('builtins.print')
    def test_lizard_vs_paper(self, mock_print):
        result = determine_winner("lizard", "paper")
        self.assertEqual(result, "You win!")

    @patch('builtins.print')
    def test_lizard_vs_scissors(self, mock_print):
        result = determine_winner("lizard", "scissors")
        self.assertEqual(result, "Computer wins!")

    @patch('builtins.print')
    def test_lizard_vs_lizard(self, mock_print):
        result = determine_winner("lizard", "lizard")
        self.assertEqual(result, "It's a tie!")

    @patch('builtins.print')
    def test_lizard_vs_spock(self, mock_print):
        result = determine_winner("lizard", "spock")
        self.assertEqual(result, "You win!")

    @patch('builtins.print')
    def test_spock_vs_rock(self, mock_print):
        result = determine_winner("spock", "rock")
        self.assertEqual(result, "You win!")

    @patch('builtins.print')
    def test_spock_vs_paper(self, mock_print):
        result = determine_winner("spock", "paper")
        self.assertEqual(result, "Computer wins!")

    @patch('builtins.print')
    def test_spock_vs_scissors(self, mock_print):
        result = determine_winner("spock", "scissors")
        self.assertEqual(result, "You win!")

    @patch('builtins.print')
    def test_spock_vs_lizard(self, mock_print):
        result = determine_winner("spock", "lizard")
        self.assertEqual(result, "Computer wins!")

    @patch('builtins.print')
    def test_spock_vs_spock(self, mock_print):
        result = determine_winner("spock", "spock")
        self.assertEqual(result, "It's a tie!")

if __name__ == '__main__':
    unittest.main()
