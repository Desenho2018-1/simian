import unittest
from simian.sprite.sprite import Sprite


class SpriteTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.filename = "image.png"
        self.sprite = Sprite(self.filename) 

    def test_rezise(self):
        current_width = self.sprite.get_width()
        current_height = self.sprite.get_height()

        self.sprite.resize(2 * current_width, 2 * current_height)

        new_width = self.sprite.get_width()
        new_height = self.sprite.get_height()

        self.assertEqual(new_width, 2 * current_width)
        self.assertEqual(new_height, 2 * current_height)

    def test_set_x(self):
        self.sprite.set_x(100)

        self.assertEqual(self.sprite.get_x(), 100)

    def test_get_x(self):
        self.sprite.set_x(100)

        self.assertEqual(self.sprite.get_x(), 100)

    def test_set_y(self):
        self.sprite.set_y(200)

        self.assertEqual(self.sprite.get_y(), 200)

    def test_get_y(self):
        self.sprite.set_y(200)

        self.assertEqual(self.sprite.get_y(), 200)
