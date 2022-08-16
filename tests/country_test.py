import unittest
from models.country import Country
import repositories.country_repository as country_repository

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Scotland", 1)

    def test_name(self):
        self.assertEqual("Scotland", self.country.name)

    def test_id(self):
        self.assertEqual(1, self.country.id)

    def test_select_id(self):
        country = country_repository.select(1)
        self.assertEqual(self.country.name, country.name)