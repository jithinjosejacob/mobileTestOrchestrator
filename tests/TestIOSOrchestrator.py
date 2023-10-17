import sys 

sys.path.append("..")

from IOS.IOSOrchestrator import IOSOrchestrator 
import unittest 


class TestIOSOrchestrator(unittest.TestCase):
    def test_orchestrator(self):
        iOSOrchestrator = IOSOrchestrator()
        iOSOrchestrator.execute_tests()





if __name__=="__main__":
    unittest.main()






