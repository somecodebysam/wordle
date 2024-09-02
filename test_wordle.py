import unittest
from wordle import wordle

class TestWordle(unittest.TestCase):

    def setUp(self):
        self.secret_word = "apple"
        self.words = ["apple", "grape", "pearl", "plumb", "table"]
        self.game = wordle(self.secret_word, self.words)
    
    def test_valid_guess_length(self):
        self.assertTrue(self.game.valid_guess_length("apple"))
        self.assertFalse(self.game.valid_guess_length("app"))

    def test_valid_guess(self):
        self.assertTrue(self.game.valid_guess("apple"))
        self.assertFalse(self.game.valid_guess("oranges"))

    def test_can_attempt(self):
        self.assertTrue(self.game.can_attempt())
        self.game.prev_attempts = ["guess1", "guess2", "guess3", "guess4", "guess5", "guess6"]
        self.assertFalse(self.game.can_attempt())

    def test_attempts_left(self):
        self.assertEqual(self.game.attempts_left(), 6)
        self.game.prev_attempts.append("guess1")
        self.assertEqual(self.game.attempts_left(), 5)

    def test_is_winner(self):
        self.assertTrue(self.game.is_winner("apple"))
        self.assertFalse(self.game.is_winner("grape"))

if __name__ == "__main__":
    unittest.main()
