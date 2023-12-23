# Import the pygame module
import pygame
from Button import Button

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Apple Trivia Quiz")
pygame.display.set_caption("Button Example")

font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def quit_game():
    pygame.quit()
    exit()

def main():
    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    quit_button = Button(400, 300, 200, 50, "Quit", quit_game)

    button_center = ((SCREEN_WIDTH - quit_button.get_width()) / 2,(SCREEN_HEIGHT - quit_button.get_height()) / 2 )

    all_sprites.add(quit_button)

    # Main loop

    # Variable to keep the main loop running
    running = True
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

        # Update all sprites
        all_sprites.update()

        # Clear the screen
        screen.fill(WHITE)

        # Draw your game elements here
        draw_text("Welcome to Apple Trivia!", 200, 100, RED)

        # Draw all sprites
        #all_sprites.draw(screen)

        screen.blit(quit_button.image, button_center)


        # Draw your game elements here
        draw_text("Quit", 400, 300, (0, 0, 0))  # Black color for the text

        # Update the display
        pygame.display.flip()



if __name__ == '__main__':
    main()

