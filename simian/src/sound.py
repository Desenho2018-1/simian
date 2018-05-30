import pygame
import logging

"""
This class creates a controller to musics on game
"""

"""
Variables used to define state and default music path
"""
music_name = "../assets/music/"
PLAY_ONCE = 0
PLAY_LOOPING = -1


class Sound:

    def __init__(self, music_name):
        self.music_name = music_name
        pygame.mixer.init()

    """
    Used to play music in an infinite loop
    """
    def play_music(self):
        assert self.music_name != "", "INVALID NAME"

        try:
            logging.info("Load music" + self.music_name)
            pygame.mixer.music.load(music_name + self.music_name)

            logging.info("Play music" + self.music_name)
            pygame.mixer.music.play(PLAY_LOOPING)

            return True
        except:
            logging.info("Music file couldn't be found")
            return False

    def stop_music(self):
        pygame.mixer.music.stop()
