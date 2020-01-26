import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testname(self):
        driver = webdriver.Chrome(
            executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        driver.get("https://www.google.com")
        titleofPage = driver.title

        # AssertEqual
        self.assertEqual("Google", titleofPage)

        # AssertNotEqual
        # self.assertNotEqual("Google123", titleofPage)


if __name__ == "__main__":
    unittest.main()
