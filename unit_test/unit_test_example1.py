import unittest
from demo_example1 import Sample1


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        Sample1.add(self,5, 15)

    def test_subtraction(self):
        Sample1.sub(self, 2, 7)





if __name__ == '__main__':
    unittest.main()
