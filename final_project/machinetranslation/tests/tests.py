import unittest
from translator import english_to_french, french_to_english

class Test_Translator(unittest.TestCase): 
    def test_english_to_french_null(self): 
        self.assertEqual(english_to_french(None),None)

    def test_french_to_english_null(self):
        self.assertEqual(french_to_english(None),None)

    def test_english_to_french_hello(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_bonjour(self): 
        self.assertEqual(english_to_french("Bonjour"), "Bonjour")

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_french_to_english_hello(self):
        self.assertEqual(french_to_english("Hello"), "Hello")

unittest.main()