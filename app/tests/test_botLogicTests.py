import unittest
from bot import Bot


#Starting with py bot message list test
class Testsbot(unittest.TestCase):
    """A class to tests all the PyBot's Logics"""
    
    def test_SwdFile(self):
        """
        """
        pass
    def test_chekcIn(self):
        obj = Bot('Salut le monde')
        obj.stopWd()
        question = 'bonjour'
        self.assertEqual(question, ['bonjour'])


            
if __name__ == '__main__':
    unittest.main()