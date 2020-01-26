import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get all the tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suites
'''Login and SignUp Tests will come into Sanity Test Suite'''
sanityTestSuite = unittest.TestSuite([tc1, tc2])    # Sanity Test Suite
# unittest.TextTestRunner().run(sanityTestSuite)

'''Payment and PaymentReturns Test will come into Functional Test Suite'''
functionalTestSuite = unittest.TestSuite([tc3, tc4])    # Functional Test Suite
# unittest.TextTestRunner().run(functionalTestSuite)

'''Rest all the test cases will fall under Master Test Suite'''
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # Master Test Suite
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)