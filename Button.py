import pygame
from pygame.locals import MOUSEBUTTONDOWN

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, callback, font=None, font_size=24, text_color=(255, 255, 255), button_color=(144, 238, 144)):
        super().__init__()

        # Create a font for the button text
        self.font = pygame.font.Font(font, font_size) if font else pygame.font.Font(None, font_size)

        # Create the button's image and rectangle
        self.image = pygame.Surface((width, height))
        self.image.fill(button_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = width
        self.height = height

        # Set up the text parameters
        self.text = text
        self.text_color = text_color

        # Set up the callback function for the button
        self.callback = callback

        # Render the text onto the button's surface
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
        self.image.blit(text_surface, text_rect)

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
