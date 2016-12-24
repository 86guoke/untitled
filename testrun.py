#coding=utf-8
import unittest
import t,t2

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(t.shouji2))
    suite.addTest(unittest.makeSuite(t2.shouji2))
    unittest.TextTestRunner(verbosity=2).run(suite)
