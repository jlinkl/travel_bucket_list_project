import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("James", 1)

    def test_name(self):
        self.assertEqual("James", self.user.name)

    def test_id (self):
        self.assertEqual(1, self.user.id)