"""


Assertions

Assertion is nothing but the check point or  you can say it as verification for the
test case to evaluate some item on the execution.

If we  do not provide  any assertion inside a test case then there is
no way to know whether a test case is failed or not.

Assertion helps in report generation based on the assertion
 the test exectuiton report will be generated.

There are few assertion which will accept all the values
and few assertions will accept only numeric values.

assertEqual
assertEqual compare the first parameter witht he seccond parametere. If both matches the unittest
will  continue with the remaining execution but both the values are different the unit test
fails the test case.


assertNotEqual

assertNotEqual method compares the given two parameters, if both paramtere are not same
then the unittest passes he test case but f both parameter are same then unittest fails the test case.



"""

import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print (self.driver.title)
        titleofwebpage=self.driver.title


        #assertEqual

        self.assertEqual("Google",titleofwebpage,"Webpage title is not same")
        ##Syntax assertEqual(output expected, output got, error message if occured)

        #self.assertEqual("Google12", titleofwebpage, "Webpage title is not same")
        ##Syntax assertEqual(output expected, output got, error message if occured)

        self.assertNotEqual("Google123", titleofwebpage, "Webpage title is not same")
        ##Syntax assertEqual(output expected, output got, error message if occured)


if __name__ == "__main__":
    unittest.main()



