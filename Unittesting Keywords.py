"""
Every test method will start with tthe test keyword

Agenda

Python Unittest Framework

setup

In a class , multiple test methods are created. On using this with setup,
this will execute before every test methods

teardown

Teardown is opposite to setup.
This will execute multiple times after completion of every test method within the class


setUpClass
tearDownClass
setUpModule
tearDownModule

"""



### Test methods

import unittest


def setUpModule(): #Before a module is started, it executes. has to called outside class
    print ("setUpModule")

def tearDownModule():##After a module is completed, it executes. has to called outside class
    prnt ()


class AppTesting(unittest.TestCase):

    ##setup method is created . It will execute before every test method
    @classmethod
    def setUp(self): #Execute before all the test methods
        print("This is a login test(setup test)")

    @classmethod #Execute after all the test methods
    def tearDown(self):
        print ("This is  logout test\n")

    @classmethod
    def setUpClass(cls): #Executes onlu once after the Class started
        print ("Application Opens\n")

    @classmethod #decorator
    def tearDownClass(cls): #Executes onlu once after the Class ended
        print ("\nApplication Closed")

    def test_search(self):
        print ("This is a search test")

    def test_advancedsearch(self):
        print ("This is Advanced search test")

    def test_prepaidrecharge(self):
        print("This is a prepaid Recharge test")

    def test_postpaidrecharge(self):
        print("This is a postpaid Recharge test")


if __name__=="__main__":
    unittest.main()