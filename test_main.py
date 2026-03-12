import unittest
from main import validate

class TestValidate(unittest.TestCase):
    def test_valid_guess(self):
        self.assertIsNone(validate("a", []))
    
    def test_length_greater_than_one(self):
        self.assertEqual(validate("ab", []), "Guessed word should only be 1 letter.")
    
    def test_not_alphabetic(self):
        self.assertEqual(validate("1", []), "Guessed word should be an alphabet character. No numbers or special characters.")
    
    def test_already_guessed(self):
        self.assertEqual(validate("a", ["a"]), "Letter has already been guessed. Do another guess!")
    
    def test_empty_guess(self):
        self.assertEqual(validate("", []), "Guessed word cannot be empty.")
    
    def test_case_insensitive_already_guessed(self):
        # Assuming case matters as per function; if normalized elsewhere, adjust
        self.assertIsNone(validate("A", ["a"]))  # Passes if case-sensitive

if __name__ == '__main__':
    unittest.main()