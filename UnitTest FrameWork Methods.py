"""
Python UnitTest Framework Methods
1. setup - This will be executed multiple time before executing the methods
2. teardown - This method will execute after completion of every test method within the class.
3. setUpClass -
4. tearDownClass
5. setUpModule - are always outside of class
6. tearDownModule - are always outside of class
"""
import unittest

def setUpModule(): # this will execute before the class has started
    print('setUpModule')

def tearDownModule():   # after completion of class methods it will execute
    print('tearDownModule')


class AppTesting(unittest.TestCase):

    # setup Method : Will execute multiple times
    @classmethod
    def setUp(self):
        print("This is login test.")

    # teardown Method : Will execute multiple times after all test methods
    @classmethod
    def tearDown(self):
        print("This is logout.")

    # SetUpClass : Execute once when the class is started
    @classmethod
    def setUpClass(self):
        print('Open Applications')

    # tearDownClass : Execute once after the class has completed
    @classmethod
    def tearDownClass(self):
        print('Close Applications')

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid Recharge test")


if __name__ == "__main__":
    unittest.main()