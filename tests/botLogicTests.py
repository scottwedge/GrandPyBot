import unittest
from app import app


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
        self.wlc = welcoming
        
        self.assertIn(messageBot('s'), self.success)
        self.assertIn(messageBot('f'), self.faild)
        self.assertIn(messageBot('w'), self.wlc)


            
if __name__ == '__main__':
    unittest.main()