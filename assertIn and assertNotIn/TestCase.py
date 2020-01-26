"""
assertIn : method verifies whether the first element is present in the second element.
If first element is present in second element then test passed or else failed.

assertNotIn : method verifies whether the first element is not present in the second
or not. If first element is present then the test will be failed or else passed.

"""
import unittest


class MyTestCase(unittest.TestCase):
    def testName(self):
        list = {"python", "selenium", "c", "java"}

        # self.assertIn("python", list)

        self.assertNotIn("alpha", list)


if __name__ == "__main__":
    unittest.main()
