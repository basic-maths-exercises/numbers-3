import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for i in range(50) :
            val = np.random.randint(1,9999)
            arr = getNumberArray(val) 
            for j in range(4) : 
                ppp = 10**(3-j)
                vv = int(np.floor( val / ppp ) )
                val = val - vv*ppp
                self.assertTrue( vv==arr[3-j], "Your function is not working" )
