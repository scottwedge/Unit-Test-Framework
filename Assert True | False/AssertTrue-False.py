import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testname(self):
        driver = webdriver.Chrome(
            executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        driver.get("https://www.google.com")
        titleofPage = driver.title

        # self.assertTrue("Google" == titleofPage)    # True

        self.assertFalse("Google" != titleofPage)  # False


if __name__ == "__main__":
    unittest.main()
