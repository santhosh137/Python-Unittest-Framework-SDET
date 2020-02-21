""""
Agenda

skipping test
    skip test
    skip test with the reason
    skip test with based on condition

skip some  test methods

3 methods are there to skip test

1. skip test based on reason
2. skip test based on condition
"""

import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest ## skipping the search test
    def test_search(self):
        print ("This is a search test")

    @unittest.skip("I am skipping this test method, bcoz it is not yet ready")
    def test_advancedsearch(self):
        print ("This is advanced search")


    @unittest.skipIf("Skipping due to some condition",1==1)
    def test_prepaidrecharge(self):
        print ("This is a prepadi recharge")

    def test_postpaidrecharge(self):
        print ("This is a post paid recharge")

    def test_loginbyemail(self):
        print("This is loging by email")

    def test_loginbytwitter(self):
        print("This is a login  by twitter")


if __name__=="__main__":
    unittest.main()