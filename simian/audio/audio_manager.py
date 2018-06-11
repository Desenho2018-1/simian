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
    Used to call music class functions and
    play a single music in an infinite loop
    """
    def play_music(self, music_path):
        self.music = Music(music_path)
        self.music.play()
        return True

    """
    Used to stop an already playing music
    """
    def stop_music(self):
        if self.music is not None:
            self.music.stop()
        else:
            raise Exception('There is no music playing right now')

    """
    Used to fade out an already playing music
    """
    def fade_out_music(self, fade_out_time):
        if self.music is not None:
            self.music.fade_out(fade_out_time)
        else:
            raise Exception('There is no music playing right now')

    """
    Used to add a sound to a list of available sounds that can be
    used by pygame
    """
    def add_sound(self, sound_path):
        if len(self.sounds) < 8:
            self.sounds.append(sound_path)
            return True
        else:
            raise Exception('Maximum number of sounds per object exceeded')

    """
    Used to play a sound previously added to the list
    """
    def play_sound(self, sound_object):
        if sound_object in self.sounds:
            self.sound = Sound(sound_object)
            self.sound.play()
        else:
            raise Exception('This sound is not a part of the list')

    """
    Used to stop an already playing sound
    """
    def stop_sound(self, sound_path):
        if sound_path in self.sounds:
            self.sound.stop()
        else:
            raise Exception('This sound is not a part of the list')

    """
    Used to fade out an already playing sound
    """
    def fade_out_sound(self, sound_path, fade_out_time):
        if sound_path in self.sounds:
            self.sound.fade_out(fade_out_time)
        else:
            raise Exception('This sound is not a part of the list')
