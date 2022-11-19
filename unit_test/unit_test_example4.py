import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("class will execute only once before all the test")

    @classmethod
    def tearDownClass(cls):
        print("It will execute after all the test")

    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")



if __name__ == '__main__':
    unittest.main()
