import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(
            executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        self.driver.get("https://www.google.com")
        print("Title of the page is : " + self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome(
            executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        self.driver.get("https://bing.com/")
        print("Title of the page is : " + self.driver.title)


if __name__ == "__main__":
    unittest.main()
