import unittest
from backuper import app

class TestStringMethods(unittest.TestCase):

    def test_noargs(self):
        self.assertEqual(app.config_changer(None), FileNotFoundError)
    def test_nofile(self):
        self.assertEqual(app.config_changer({False, False, None, None, 0, 0, False}), FileNotFoundError)


if __name__ == '__main__':
    unittest.main()
