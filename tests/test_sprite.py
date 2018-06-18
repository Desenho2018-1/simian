import unittest
from simian.sprite import Sprite
from simian.config import Configuration


class SpriteTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.filename = "engineer.jpg"
        self.sprite = Sprite(self.filename)

    def test_rezise(self):
        current_width = self.sprite.width
        current_height = self.sprite.height

        self.sprite.resize(2 * current_width, 2 * current_height)

        new_width = self.sprite.width
        new_height = self.sprite.height

        self.assertEqual(new_width, 2 * current_width)
        self.assertEqual(new_height, 2 * current_height)

    def test_set_x(self):
        self.sprite.x = 100

        self.assertEqual(self.sprite.x, 100)

    def test_get_x(self):
        self.sprite.x = 100

        self.assertEqual(self.sprite.x, 99.5)

    def test_set_y(self):
        self.sprite.y = 200

        self.assertEqual(self.sprite.y, 200)

    def test_get_y(self):
        self.sprite.y = 200

        self.assertEqual(self.sprite.y, 199.5)
