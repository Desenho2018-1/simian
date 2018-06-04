import unittest
from simian.audio.audios import Sound, Music
from simian.audio.audio_manager import AudioManager

class SoundTest(unittest.TestCase):
    def setUp(self):
        self.audio_manager = AudioManager()

    def test_play_sound(self):
        sound = Sound('assets/audio/sound.wav')
        self.assertTrue(sound.play())

    def test_play_music(self):
        music = Music('assets/audio/music.mp3')
        self.assertTrue(music.play())


class AudioManagerTest(unittest.TestCase):
    def test_constructor_music(self):
        self.audio_manager = AudioManager()
        self.assertTrue(self.audio_manager.music is None)
        self.assertTrue(not self.audio_manager.sounds)

    def test_play_music(self):
        self.audio_manager = AudioManager()
        response = self.audio_manager.play_music('assets/audio/music.mp3')
        self.assertTrue(response)
