import unittest
from models.attraction import Attraction

class TestAttraction(unittest.TestCase):
    def setUp(self):
        self.attraction = Attraction("Scott Monument", 1, 1)

    def test_name(self):
        self.assertEqual("Scott Monument", self.attraction.name)

    def test_id(self):
        self.assertEqual(1, self.attraction.id)

    def test_city_id(self):
        self.assertEqual(1, self.attraction.city_id)