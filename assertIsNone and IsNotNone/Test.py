"""
assertIsNone should return nothing and not should return a value to pass the test
"""
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        # driver = webdriver.Chrome(
        #     executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        driver = None

        self.assertIsNone(driver)   # True if no value is there

        # self.assertIsNotNone(driver)


if __name__ == "__main__":
    unittest.main()
