import pygame

class SoundManager:
        def pause_all(self):
            pygame.mixer.pause()

        def unpause_all(self):
            pygame.mixer.unpause()
