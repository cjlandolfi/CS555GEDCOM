import unittest
import Parser as Parser
from US02 import US02
from US03 import US03
from US04 import US04
from US06 import US06
from US07 import US07
from US11 import US11
from US16 import US16
from US17 import US17
from US21 import US21

class TestAllUserStories(unittest.TestCase):
    def test_US02(self):
        self.assertEqual(US02('@F3@'), True)

    def test_US03(self):
        self.assertEqual(US03('@I11@'), True)

    def test_US04(self):
        self.assertEqual(US04('@F2@'), True)

    def test_US06(self):
        self.assertEqual(US06('@F2@'), True)

    def test_US07(self):
        self.assertEqual(US07('@I8@'), True)

    def test_US11(self):
        self.assertEqual(US11('@I13@'), True)

    def test_US16(self):
        self.assertEqual(US16('@F1@'), True)

    def test_US17(self):
        self.assertEqual(US17('@F6@'), True)

    def test_US21(self):
        self.assertEqual(US21('@F1@'), True)

if __name__ == '__main__':
	unittest.main()