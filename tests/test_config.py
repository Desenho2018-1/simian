import unittest
import os
from simian.config import Configuration


class ConfigTest(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.config_file_path = os.path.join(dirname, 'config/config.ini')
        self.config = Configuration(self.config_file_path)
        self.test_image_assets_path = os.path.join(dirname, 'assets/images')
        self.test_audio_assets_path = os.path.join(dirname, 'assets/audios')

    def test_constructor(self):
        self.assertEqual(self.config.IMAGE_ASSETS_PATH,
                         self.test_image_assets_path)
        self.assertEqual(self.test_audio_assets_path,
                         self.config.AUDIO_ASSETS_PATH)
