import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Scotland", 1)

    def test_name(self):
        self.assertEqual("Scotland", self.country.name)

    def test_id(self):
        self.assertEqual(1, self.country.id)