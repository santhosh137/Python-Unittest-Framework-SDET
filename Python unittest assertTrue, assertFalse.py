"""
assertTrue

when we have only two parameter we can use assertEqual method to check whether
both are same or not, but if we have more than two parameters, comparing values
with assertEqual method become more difficult

assertTrue method checks whether the given parameter is true or not, if  the value is
true then test is passed otherwise test is failed.

assertFalse

assertFalse method compares whether given value or expression results in false or not.

If the result or value is false then unitttest passes the testcase but if the result
or value is true then unittest fails the test case.


"""

import unittest

from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        self.driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        titleofwebpage=(self.driver.title)

        self.assertTrue(titleofwebpage=="Google")

        self.assertFalse(titleofwebpage=="Google143")


if __name__=="__main__":
    unittest.main()







