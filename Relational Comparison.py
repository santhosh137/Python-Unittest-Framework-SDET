"""

Relational Comparison

assertGreater verifies whetheht the first values if greater than second vale or not.

assertGreaterEqual verifies whether the first parameter is greater or equal to the
second parameter

assertLess verifies whether the first parameter is lesser than the second parameter or not.

assertlessEqual verifies whether the first parameter is lesser that or equal to the second parameter.



"""

import unittest

class Test (unittest.TestCase):
    def testName(self):
        self.assertGreater(109,10)
        self.assertGreaterEqual(109,10)
        self.assertGreaterEqual(100,100)
        self.assertLess(19,100)
        self.assertEqual(19,100)
        self.assertEqual(100,100)


if __name__== "__main__":
    unittest.main()

