"""

assertIn
assertIn method verifies whether the first element is present in the send element,
if first element is present in second element then the tests passed  otherwise
it is failed.



assertNotIN
assertNotin method verifies whether the first element is not presnet in the second element or not,
if the first element is present then the test will be failed otherwise test is passed.

These two methods will be helpful when you want to verify the presence of value in a list tuple set and
dictionary


"""

import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def test(self):
        list=["python","selenium","java"]
        self.assertIn("python",list)
        #self.assertIn("Ruby",list)
        self.assertNotIn("Ruby",list)
        #self.assertNotIn("python",list)

if __name__== "__main__":
    unittest.main()



