import pygame
from simian.audio.audios import Audio, Music, Sound

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.audios = []
        self.music = None

    def pause_all(self):
        pygame.mixer.pause()

    def unpause_all(self):
        pygame.mixer.unpause()

    def play_music(self, music_path):
        self.music = Music(music_path)
        self.music.play()
