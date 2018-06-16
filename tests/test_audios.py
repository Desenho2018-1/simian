import unittest
import pygame
from simian.audio.audios import Sound, Music
from simian.audio.audio_manager import AudioManager


class SoundTest(unittest.TestCase):

    def setUp(self):
        self.audio_manager = AudioManager()

    def test_should_create_sound(self):
        try:
            sound = Sound('sound.wav')
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
        sound = Sound('sound.wav')
        self.assertTrue(sound.play())

    def test_should_not_play_sound(self):
        try:
            sound = Sound('doesnt_exist.wav')
            sound.play()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_play_music(self):
        music = Music('music.mp3')
        self.assertTrue(music.play())


class AudioManagerTest(unittest.TestCase):

    def test_should_construct_music(self):
        self.audio_manager = AudioManager()
        self.assertTrue(self.audio_manager.music is None)
        self.assertTrue(not self.audio_manager.sounds)

    def test_should_play_music(self):
        self.audio_manager = AudioManager()
        response = self.audio_manager.play_music('music.mp3')
        self.assertTrue(response)

    def test_should_not_play_music(self):
        self.audio_manager = AudioManager()

        try:
            self.audio_manager.play_music('doesnt_exist.mp3')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_stop_music(self):
        self.audio_manager = AudioManager()
        self.audio_manager.play_music('music.mp3')

        try:
            self.audio_manager.stop_music()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_should_not_stop_music(self):
        self.audio_manager = AudioManager()

        try:
            self.audio_manager.stop_music()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_fade_out_music(self):
        self.audio_manager = AudioManager()
        self.audio_manager.play_music('music.mp3')

        try:
            self.audio_manager.fade_out_music(1)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_should_not_fade_out_music(self):
        self.audio_manager = AudioManager()

        try:
            self.audio_manager.fade_out_music(1)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_add_sound(self):
        self.audio_manager = AudioManager()
        self.assertTrue(self.audio_manager.add_sound('sound.wav'))

    def test_should_play_sound(self):
        self.audio_manager = AudioManager()
        self.audio_manager.add_sound('sound.wav')

        try:
            self.audio_manager.play_sound('sound.wav')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_should_not_play_sound(self):
        self.audio_manager = AudioManager()

        try:
            self.audio_manager.play_sound('doesnt_exist')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_stop_sound(self):
        self.audio_manager = AudioManager()
        self.audio_manager.add_sound('sound.wav')
        self.audio_manager.play_sound('sound.wav')

        try:
            self.audio_manager.stop_sound('sound.wav')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_should_not_stop_sound(self):
        self.audio_manager = AudioManager()

        try:
            self.audio_manager.fade_out_sound('sound.wav')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_fade_out_sound(self):
        self.audio_manager = AudioManager()
        self.audio_manager.add_sound('sound.wav')
        self.audio_manager.play_sound('sound.wav')

        try:
            self.audio_manager.fade_out_sound('sound.wav', 1)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_should_not_fade_out_sound(self):
        self.audio_manager = AudioManager()

        try:
            self.audio_manager.fade_out_sound('sound.wav', 1)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
