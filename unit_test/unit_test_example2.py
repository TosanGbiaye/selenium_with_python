import unittest


class MyTestCase(unittest.TestCase):
    def test_addNumbers(self):
        print(5 +6)
        self.assertEqual(11, 11)

    def test_subNumbers(self):
        print(8 - 1)
        self.assertEqual(7,7)

        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
