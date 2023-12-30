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
    MOUSEBUTTONDOWN,
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

# Game States
MAIN_MENU = 0
GAMEPLAY = 1


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Apple Trivia Quiz")
pygame.display.set_caption("Button Example")

font = pygame.font.Font(None, 36)


def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def start_game():
    print("Start game function (to be implemented)")

def quit_game():
    pygame.quit()
    exit()

def calculate_center(width, height):
    center_x = (SCREEN_WIDTH - width) / 2
    center_y = (SCREEN_HEIGHT - height) / 2
    return center_x, center_y

###################################
#Button


all_sprites = pygame.sprite.Group()

button_width = 200
button_height = 50

quit_button = Button(*calculate_center(button_width, button_height - 150), button_width, button_height, "Quit", quit_game)
start_button = Button(*calculate_center(button_width, button_height), button_width, button_height, "Start", start_game)

all_sprites.add(quit_button, start_button)

#####################################

def handle_main_menu_events(event):
    # Handle events for the main menu state
    if event.type == MOUSEBUTTONDOWN:
        if start_button.rect.collidepoint(event.pos):
            # Transition to the gameplay state when the "Start" button is clicked
            return GAMEPLAY

    return MAIN_MENU  # Return the current state if no state change

def update_main_menu():
    # Update logic for the main menu state
    pass

def draw_main_menu():
    # Clear the screen
    screen.fill(WHITE)

    # Draw elements for the main menu state
    draw_text("Welcome to Apple Trivia!", 200, 100, RED)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

def handle_gameplay_events(event):
    # Handle events for the gameplay state
    if event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            # Transition back to the main menu when ESC is pressed
            return MAIN_MENU

    return GAMEPLAY  # Return the current state if no state change
    pass

def update_gameplay():
    # Update logic for the gameplay state
    pass

def draw_gameplay():
    # Draw elements for the gameplay state
    pass

def main():


    # Initialize game state
    current_state = MAIN_MENU


    # Main loop

    # Variable to keep the main loop running
    running = True
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif current_state == MAIN_MENU:
                current_state = handle_main_menu_events(event)
            elif current_state == GAMEPLAY:
                handle_gameplay_events(event)

            # Update and draw based on the current state
            if current_state == MAIN_MENU:
                update_main_menu()
                draw_main_menu()
                # Pass the event to each sprite individually
                for sprite in all_sprites:
                    sprite.handle_event(event)
            elif current_state == GAMEPLAY:
                update_gameplay()
                draw_gameplay()




        # Draw your game elements here
        #draw_text("Quit", 400, 300, (0, 0, 0))  # Black color for the text

        # Update the display
        pygame.display.flip()



if __name__ == '__main__':
    main()

