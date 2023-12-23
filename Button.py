import pygame
from pygame.locals import MOUSEBUTTONDOWN

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, callback):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.width = width
        self.height = height
        self.image.fill((144, 238, 144))  # Red color for the button
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.callback = callback

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def update(self):
        # You can add custom update logic for the button here
        pass

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.rect.collidepoint(x, y):
                self.callback()
