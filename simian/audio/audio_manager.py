import pygame
from simian.audio.audios import Audio, Music, Sound

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = []
        self.sounds = self.sounds[:8]
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
    def add_sound(self, sound_path):
        try:
            new_sound = Sound(sound_path)
        except:
            raise Exception('Could not create sound object')

        if len(sounds) < 8:
            self.sounds.append(new_sound)
            return True
        else:
            raise Exception('Maximum number of sounds per object exceeded')

    """
    Used to play a sound previously added to the list
    """
    def play_sound(self, sound_object):
        if sound_object in self.sounds:
            current_sound = self.sounds.index(sound_object)
            self.sounds[current_sound].play()
        else:
            raise Exception('Sound Object is not a part of the list')
