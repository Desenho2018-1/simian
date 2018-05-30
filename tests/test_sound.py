import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from simian.src.sound import *

class SoundTest(unittest.TestCase):

    def test_play_music(self):
        sound = Sound('test.mp3')
        self.assertTrue(sound.play_music())
