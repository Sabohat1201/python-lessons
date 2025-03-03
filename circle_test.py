import unittest
from circle import getArea,getPerimetr
class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5),78.53975,3)
        self.assertAlmostEqual(getArea(10),314.159,3)
    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(10),62.8318,3)
        self.assertAlmostEqual(getPerimetr(4),25.1327,3)
unittest.main()