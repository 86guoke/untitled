#coding=utf-8
import unittest
import t2
class shouji2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=t2.shouji2.test_get()

    def test_get(self):
        self.driver.

    def setUp(self):
        print "setup1"

    def test_a(self):
        print "t1"

    def tearDown(self):
        print "tearDown"
    @classmethod
    def tearDownClass(cls):
        print "tearDownclass"

if __name__=="__main__":
    unittest.main()
