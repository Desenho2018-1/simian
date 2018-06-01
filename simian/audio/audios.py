import pygame
import logging
from abc import ABC, abstractmethod

"""
This class creates a controller to musics on game
"""

"""
Variables used to define state and default music path
"""
MUSIC_PATH = "simian/assets/music/"
PLAY_ONCE = 0
PLAY_LOOPING = -1

class Audio(ABC):

    def __init__(self, music_path):
        self.music_path = music_path

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fade_out(self, time):
        pass

class Sound(Audio):
    """
    Used to play sound effects on a game, with maximum of eight being played
    played at once in a game.
    """
    def __init__(self, music_path):
        Audio.__init__(self, music_path)
        self.sound = pygame.mixer.Sound(music_path)

    def play(self):
        try:
            self.sound.play()
        except:
            logging.info("Sound file couldn't be found")

    def stop(self):
        self.sound.stop()

    def fade_out(self, time):
        self.sound.fade_out()

class Music(Audio):
    """
    Used to play music in an infinite loop, only one music can be played at once
    in a game.
    """
    def __init__(self, music_path):
        Audio.__init__(self, music_path)
        self.sound = pygame.mixer.Sound(music_path)

    def play(self):
        assert self.music_name != "", "INVALID NAME"

        try:
            logging.info("Load music" + self.music_name)
            pygame.mixer.music.load(MUSIC_PATH + self.music_name)

            logging.info("Play music" + self.music_name)
            pygame.mixer.music.play(PLAY_LOOPING)

            logging.info("Looping music")
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(100000000)
            return True
        except:
            logging.info("Music file couldn't be found")
            return False

    def stop(self):
        pygame.mixer.music.stop()
