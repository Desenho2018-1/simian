import pygame
import logging
from abc import ABC, abstractmethod
from simian.config import Configuration

"""
Variables used to define state
"""
PLAY_ONCE = 0
PLAY_LOOPING = 0


AUDIO_PATH = Configuration().AUDIO_ASSETS_PATH


class Audio(ABC):

    def __init__(self, filename):
        self.audio_path = AUDIO_PATH + filename

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
    The sound file must be an OGG audio file or from an uncompressed WAV
    """
    def __init__(self, filename):
        Audio.__init__(self, filename)
        self.sound = pygame.mixer.Sound(self.audio_path)

    def play(self):
        try:
            self.sound.play()
            return True
        except:
            logging.info("Sound file couldn't be found")

    def stop(self):
        self.sound.stop()

    def fade_out(self, time):
        self.sound.fade_out(time)


class Music(Audio):
    """
    Used to play music in an infinite loop, only one music can be played
    at once in a game.
    """
    def __init__(self, filename):
        Audio.__init__(self, filename)
        print(pygame.mixer.music.load(self.audio_path))

    def play(self):
        logging.info("Play music" + self.audio_path)
        print(pygame.mixer.music.play(PLAY_LOOPING))
        logging.info("Looping music")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        return True

    def stop(self):
        pygame.mixer.music.stop()

    def fade_out(self, time):
        pygame.mixer.music.fadeout(time)
