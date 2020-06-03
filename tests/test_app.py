import unittest


class TestStringMethods(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(app.get_results(0, 1, 1), ZeroDivisionError)


if __name__ == '__main__':
    unittest.main()