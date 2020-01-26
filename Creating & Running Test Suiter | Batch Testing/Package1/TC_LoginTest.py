import unittest


class LoginTest(unittest.TestCase):

    def test_loginbyEmail(self):
        print("Ths is login by email test.")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
            print("Ths is login by Facebook test.")
            self.assertTrue(True)

    def test_loginbyTwitter(self):
            print("Ths is login by Twitter test.")
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
