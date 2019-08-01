import unittest
from app import bot as bt



#Starting with py bot message list test
class botTests(unittest.TestCase):
    """A class to tests all the PyBot's Logics"""
    
    def testInlist(self):
        """test which list is the query in 
            to make after a best response from 
            the pybot to the user
        """
        self.success = bt.successResp
        self.faild = bt.faildResp
        self.wlc = bot.welcoming
        
        self.assertIn(bt.messageBot('s'), self.success)
        self.assertIn(bt.messageBot('f'), self.faild)
        self.assertIn(bt.messageBot('w'), self.wlc)


            
if __name__ == '__main__':
    unittest.main()