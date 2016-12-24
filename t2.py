#coding=utf-8
import unittest


class shouji2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass'
        global driver
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.dialer'
        desired_caps['appActivity'] = '.DialtactsActivity'

        cls.driver = .Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def test_get(self):
        return driver



    @unittest.skip("demonstrating skipping")
    def setUp(self):
        print "2b"

    def test_a(self):
        print "2bb"

    def tearDown(self):
        print "2c"
    @classmethod
    def tearDownClass(cls):
        print "2d"

if __name__=="__main__":
    unittest.main()
