import unittest
from backuper import backuper

class TestStringMethods(unittest.TestCase):

    def test_ftp(self):
        self.assertEqual(backuper.ftp_sender(), None)
    def test_Yandex(self):
        self.assertEqual(backuper.two_sender(), None)


if __name__ == '__main__':
    unittest.main()
