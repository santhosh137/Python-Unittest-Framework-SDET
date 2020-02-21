""""
Python Unittest framework

In automation testing, organising your code is very important and client expect us to write
automation  scripts according to the manual test cases

We can get good reporting structure if we can exacctly map our automation code with the
manual test cases.

In python we can use Unittest Testing framework to organize our automation code
and  to extract reports

To use the methods present in the usnittest framework, we have to extend the Testcase
class present in the Unittest module.


"""


import unittest

## This class should extend testcase from unittest  module
class Test(unittest.TestCase):
    def test_firstTest(self):
        print("This is my first unit test case")

if __name__=="__main__":
    unittest.main()



