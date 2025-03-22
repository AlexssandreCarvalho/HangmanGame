import pygame
from .game import HangmanGame
from .menu import Menu
import time

# Load background images (outside functions to load only once)
try:
    win_background = pygame.image.load("assets/images/win_background.png")
    lose_background = pygame.image.load("assets/images/lose_background.png")
except FileNotFoundError:
    print("Error: Background images not found! Check the paths.")
    win_background = None
    lose_background = None


def main():
    # Initialize Pygame
    pygame.init()
    # Create an instance of the Menu class
    menu = Menu()

    # Set the game loop to running
    running = True
    # Main game loop
    while running:
        # Draw the menu
        menu.draw()
        # Get the selected option from the menu
        choice = menu.get_selection()

        # If the player chooses to play the game
        if choice == "play":
            # Stop the menu music before starting the game
            pygame.mixer.music.stop()
            # Create an instance of the HangmanGame class
            game = HangmanGame("assets/word_list.txt")
            # Run the game loop and store the return value
            game_running = game_loop(game)
            # If the game loop returns False, break to return to the menu
            if not game_running:
                continue
            # Load the menu music again
            pygame.mixer.music.load("assets/menu_music.mp3")
            # Play the menu music again
            pygame.mixer.music.play(-1)
        # If the player chooses to view the score
        elif choice == "score":
            # Implement the logic to display the scores here
            pass
        # If the player chooses to exit the game
        elif choice == "exit":
            # Set running to False to exit the game loop
            running = False

    # Quit Pygame
    pygame.quit()


def game_loop(game):
    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()
    # Set the game loop to running
    running = True

    # Game loop
    while running:
        # Limit the frame rate to 60 frames per second
        clock.tick(60)
        # Handle events
        for event in pygame.event.get():
            # If the player quits the game
            if event.type == pygame.QUIT:
                return False
            # If the player clicks the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())
                game.draw()

        # Draw the game
        game.draw()

        # If the player wins the game
        if game.check_win():
            # Show the win message
            show_message(game.win, "You WON!", win_background)
            # Delay before returning to menu
            time.sleep(2)
            # Stop game music before returning to menu
            pygame.mixer.music.stop()
            # Return True to go back to the main loop
            return True
        # If the player loses the game
        if game.check_lose():
            # Ensure the hangman image is drawn
            game.draw()
            # Increase delay to 2 seconds
            time.sleep(2)
            # Show the lose message
            show_message(game.win, "You LOST!", lose_background)
            # Delay before returning to menu
            time.sleep(2)
            # Stop game music before returning to menu
            pygame.mixer.music.stop()
            # Return True to go back to the main loop
            return True

    return running


def show_message(win, msg, background=None):
    # If a background image is provided
    if background:
        # Draw the background image
        win.blit(background, (0, 0))
    # If no background image is provided
    else:
        # Fill the window with white
        win.fill((255, 255, 255))
    # Set the font
    font = pygame.font.SysFont("comicsans", 60)
    # Render the message
    text = font.render(msg, 1, (0, 0, 0))
    # Draw the message
    win.blit(text, (400 - text.get_width() / 2, 250 - text.get_height() / 2))
    # Update the display
    pygame.display.update()
