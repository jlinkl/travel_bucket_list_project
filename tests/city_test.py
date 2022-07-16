import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("Edinburgh", 1, 1)

    def test_name(self):
        self.assertEqual("Edinburgh", self.city.name)

    def test_id(self):
        self.assertEqual(1, self.city.id)

    def test_country_id(self):
        self.assertEqual(1, self.city.country_id)