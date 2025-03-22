import pygame
import math
import random


class HangmanGame:
    def __init__(self, words_file):
        # Initialize the mixer for music
        pygame.mixer.init()
        # Load the game music file
        pygame.mixer.music.load("assets/game_music.mp3")
        # Play the game music in a loop
        pygame.mixer.music.play(-1)
        # Define the width and height of the window
        self.WIDTH, self.HEIGHT = 800, 500
        # Set the display mode for the window
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # Setup the buttons for letter selection
        self._setup_buttons()
        # Load the assets for the game
        self._load_assets()
        # Load the words from the file
        self.words = self._load_words(words_file)
        # Reset the game state
        self.reset_game()
        # Load the background image for the game
        self.background = pygame.image.load("assets/images/game_background.png")

    def _setup_buttons(self):
        # Define the radius of the letter buttons
        self.RADIUS = 20
        # Define the gap between the letter buttons
        self.GAP = 15
        # Create a list to store the letter buttons
        self.letters = []
        # Calculate the starting x position for the letter buttons
        startx = round((self.WIDTH - (self.RADIUS * 2 + self.GAP) * 13) / 2)
        # Define the starting y position for the letter buttons
        starty = 400
        # Iterate through the alphabet and create a button for each letter
        for i in range(26):
            # Calculate the x position for the current letter button
            x = startx + self.GAP * 2 + ((self.RADIUS * 2 + self.GAP) * (i % 13))
            # Calculate the y position for the current letter button
            y = starty + ((i // 13) * (self.GAP + self.RADIUS * 2))
            # Append the button to the list of letter buttons
            self.letters.append([x, y, chr(65 + i), True])

    def _load_assets(self):
        # Load the hangman images
        self.images = [
            pygame.image.load(f"assets/images/hangman{i}.png") for i in range(7)
        ]
        # Define the font for the letters
        self.LETTER_FONT = pygame.font.SysFont("comicsans", 40)
        # Define the font for the word
        self.WORD_FONT = pygame.font.SysFont("comicsans", 60)
        # Define the font for the title
        self.TITLE_FONT = pygame.font.SysFont("comicsans", 70)
        # Define the color white
        self.WHITE = (255, 255, 255)
        # Define the color black
        self.BLACK = (0, 0, 0)

    def _load_words(self, filename):
        # Open the file and read the words
        with open(filename, "r") as file:
            # Return a list of words from the file
            return [line.strip().upper() for line in file]

    def reset_game(self):
        # Choose a random word from the list of words
        self.word = random.choice(self.words)
        # Create a list to store the guessed letters
        self.guessed = []
        # Set the hangman status to 0
        self.hangman_status = 0
        # Set the number of lives to 6
        self.lives = 6
        # Set all letters to visible
        for letter in self.letters:
            letter[3] = True

    def draw(self):
        # Blit the background image onto the window
        self.win.blit(self.background, (0, 0))
        # Draw the word
        display_word = " ".join([c if c in self.guessed else "_" for c in self.word])
        text = self.WORD_FONT.render(display_word, 1, self.BLACK)
        self.win.blit(text, (400, 200))
        # Draw the buttons
        for letter in self.letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(self.win, self.BLACK, (x, y), self.RADIUS, 3)
                text = self.LETTER_FONT.render(ltr, 1, self.BLACK)
                self.win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
        # Draw the hangman image
        self.win.blit(self.images[self.hangman_status], (150, 100))
        # Update the display to show the changes
        pygame.display.update()

    def handle_click(self, pos):
        # Get the x and y coordinates of the mouse click
        x, y = pos
        # Iterate through the letter buttons
        for letter in self.letters:
            lx, ly, ltr, visible = letter
            # If the letter is visible
            if visible:
                # Calculate the distance between the mouse click and the letter button
                distance = math.hypot(lx - x, ly - y)
                # If the distance is less than the radius of the letter button
                if distance < self.RADIUS:
                    # Set the letter to not visible
                    letter[3] = False
                    # Add the letter to the list of guessed letters
                    self.guessed.append(ltr)
                    # If the letter is not in the word
                    if ltr not in self.word:
                        # Increment the hangman status
                        self.hangman_status += 1
                    return True
        return False

    def check_win(self):
        # Check if all letters in the word have been guessed
        return all(c in self.guessed for c in self.word)

    def check_lose(self):
        # Check if the hangman status is greater than or equal to 6
        return self.hangman_status >= 6

    def game_over(self):
        return True
