"""
asertTrue & assertFalse
If conditions returns true the the test pass
"""

import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(
            executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        driver.get("https://www.google.com")

        titleofPage = driver.title

        # self.assertTrue(titleofPage == "Google")

        self.assertFalse(titleofPage == "Google1")


if __name__ == "__main__":
    unittest.main()
