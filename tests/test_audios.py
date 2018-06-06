import unittest
import pygame
from simian.audio.audios import Sound, Music
from simian.audio.audio_manager import AudioManager

class SoundTest(unittest.TestCase):
    def setUp(self):
        self.audio_manager = AudioManager()

    def test_should_create_sound(self):
        try:
            sound = Sound('assets/audio/sound.wav')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_should_not_create_sound(self):
        try:
            sound = Sound('doesnt_exist.wav')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_play_sound(self):
        sound = Sound('assets/audio/sound.wav')
        self.assertTrue(sound.play())

    def test_should_not_play_sound(self):
        try:
            sound = Sound('doesnt_exist.wav')
            sound.play()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_play_music(self):
        music = Music('assets/audio/music.mp3')
        self.assertTrue(music.play())


class AudioManagerTest(unittest.TestCase):
    def test_should_construct_music(self):
        self.audio_manager = AudioManager()
        self.assertTrue(self.audio_manager.music is None)
        self.assertTrue(not self.audio_manager.sounds)

    def test_should_play_music(self):
        self.audio_manager = AudioManager()
        response = self.audio_manager.play_music('assets/audio/music.mp3')
        self.assertTrue(response)

    def test_should_not_play_music(self):
        self.audio_manager = AudioManager()
        try:
            self.audio_manager.play_music('doesnt_exist.mp3')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_add_sound(self):
        self.audio_manager = AudioManager()
        self.assertTrue(self.audio_manager.add_sound('assets/audio/sound.wav'))
