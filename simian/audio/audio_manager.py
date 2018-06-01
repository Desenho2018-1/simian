import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()

    def pause_all(self):
        pygame.mixer.pause()

    def unpause_all(self):
        pygame.mixer.unpause()
