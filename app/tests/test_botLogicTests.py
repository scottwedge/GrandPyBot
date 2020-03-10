import unittest
from app.bot import Bot


# Starting with py bot message list test
class Testsbot(unittest.TestCase):
    """A class to tests all the PyBot's Logics"""

    def test_chekcIn(self):
        """
        """
        pass

    def test_ValueReturned(self):
        obj = Bot("bonjour")
        obj.stopWd()
        question = obj.stopWd()
        self.assertEqual(question, "bonjour")


if __name__ == "__main__":
    unittest.main()
