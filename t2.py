#coding=utf-8
import unittest


class shouji2(unittest.TestCase):
    def __init__(self):
        print "8888888888888"

    @classmethod
    def setUpClass(cls):
        print "111"


    @unittest.skip("demonstrating skipping")
    def setUp(self):
        print "2b"

    def test_a(self,name):
        print "2bbnnnnnnnnnnnnnn"+name

    def tearDown(self):
        print "2c"
    @classmethod
    def tearDownClass(cls):
        print "2d"

if __name__=="__main__":
    unittest.main()
