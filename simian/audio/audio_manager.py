import pygame
from simian.audio.audios import Audio, Music, Sound

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = sounds[:8]
        self.music = None

    def pause_all(self):
        pygame.mixer.pause()

    def unpause_all(self):
        pygame.mixer.unpause()

    """
    Used to call music class functions and play a single music in an infinite loop
    """
    def play_music(self, music_path):
        self.music = Music(music_path)
        self.music.play()
        return True

    """
    Used to add a sound to a list of available sounds that can be used by pygame
    """
    def add_sound(self, sound_object):
        if isinstance(sound_object, Sound):
            if len(sounds) < 8:
                self.sounds.append(sound_object)
                return True
            else:
                raise Exception('Maximum number of sounds per object exceeded')
        else:
            raise TypeError('Parameter must be a Sound object')
