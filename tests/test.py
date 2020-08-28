import unittest

class TestStringMethods(unittest.TestCase):

    #%% setUp, tearDown class

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    #%% setUp, tearDown

    def setUp(self):    # runs before every test
        self.s = 'hello world'

    def tearDown(self): # runs after every test
        pass            # can be used if method generates files. ie delete files after testing


    #%% Tests   # Note: tests are not ran in order
    
    def test_upper(self):   # names must start with test_
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        #s = 'hello world'
        self.assertEqual(self.s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            self.s.split(2)

if __name__ == '__main__':
    unittest.main()
