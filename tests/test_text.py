from simian.text import Text
import unittest
import pygame


class TextTest(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.text = Text('Test Content', 50, 'comicsansms')

        """test is None"""
        self.font = self.text.font

        """Instance for methods display"""
        self.text.bold(True)
        self.text.underline(True)
        self.text.italic(True)

    def tearDown(self):
        self.text = None

    def test_message(self):
        content = self.text.content
        self.assertEqual(content, 'Test Content')

    def test_size(self):
        size = self.text.size
        self.assertEqual(size, 50)

    """
        Test methods for custom text
    """

    def test_is_bold_text(self):
        is_bold = self.text.is_bold()
        self.assertEqual(is_bold, True)

    def test_is_underline_text(self):
        is_underline = self.text.is_underline()
        self.assertEqual(is_underline, True)

    def test_is_italic_text(self):
        is_italic = self.text.is_italic()
        self.assertEqual(is_italic, True)

if __name__ == '__main__':
    unittest.main()
