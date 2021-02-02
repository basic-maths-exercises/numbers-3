try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        inputs, outputs = [], []
        for i in range(50) :
            val = np.random.randint(1,9999)
            inputs.append((val,))
            oval = np.zeros(4)
            arr = getNumberArray(val) 
            for j in range(4) : 
                ppp = 10**(3-j)
                oval[j] = int(np.floor( val / ppp ) )
                val = val - oval[j]*ppp
            outputs.append( oval )
         assert( fc.check_func('getNumberArray', inputs, outputs ) )
