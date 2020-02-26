"""assertIsNone and assertIsNotNone

assertIsNone

assertIsNone method verifies whether give values or expression results in None or not,
if the result is none then python unittest will pass the test case otherwise fails the
test case

assertIsNotNone

assertIsNotNone method verifies whether give values is not None, if the value is NOne
then the test case will be failed.


"""

import unittest

from selenium import webdriver


from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.assertIsNotNone(driver)


class Test1(unittest.TestCase):
    def testName(self):
        driver = None
        self.assertIsNone(driver)


if __name__=="__main__":
    unittest.main()

