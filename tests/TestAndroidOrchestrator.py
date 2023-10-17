import sys 

sys.path.append("..")

from Android.AndroidOrchestrator import AndroidOrchestrator 

import unittest

class TestAndroidOrchestrator(unittest.TestCase):
    def test_android(self):
        androidOrchestrator = AndroidOrchestrator()

        androidOrchestrator.execute_tests()



if __name__ == "__main__":
    unittest.main()