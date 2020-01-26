import unittest


class SignupTest(unittest.TestCase):

    def test_signbyEmail(self):
        print("Ths is signby email test.")
        self.assertTrue(True)

    def test_signbyFacebook(self):
        print("Ths is sign by Facebook test.")
        self.assertTrue(True)

    def test_signbyTwitter(self):
        print("Ths is sign by Twitter test.")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
