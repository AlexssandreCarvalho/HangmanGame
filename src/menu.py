import pygame


class Menu:
    def __init__(self):
        # Initialize the mixer for music
        pygame.mixer.init()
        # Load the menu music file
        pygame.mixer.music.load("assets/menu_music.mp3")
        # Play the menu music in a loop
        pygame.mixer.music.play(-1)
        # Define the width and height of the window
        self.WIDTH, self.HEIGHT = 800, 500
        # Set the display mode for the window
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # Define the options available in the menu
        self.options = ["Start Game", "Score", "Exit"]
        # Define the font for the title
        self.TITLE_FONT = pygame.font.SysFont("comicsans", 70)
        # Define the font for the options
        self.FONT = pygame.font.SysFont("comicsans", 40)
        # Define the color white
        self.WHITE = (255, 255, 255)
        # Define the color black
        self.BLACK = (0, 0, 0)
        # Load the background image for the menu
        self.background = pygame.image.load("assets/images/menu_background.png")

    def draw(self):
        # Blit the background image onto the window
        self.win.blit(self.background, (0, 0))
        # Draw the title "HANGMAN (Demo)"
        text = self.TITLE_FONT.render("HANGMAN (Demo)", 1, self.BLACK)
        self.win.blit(text, (self.WIDTH / 2 - text.get_width() / 2, 20))
        # Iterate through the options and draw them on the screen
        for i, option in enumerate(self.options):
            text = self.FONT.render(option, 1, self.BLACK)
            self.win.blit(text, (self.WIDTH / 2 - text.get_width() / 2, 200 + i * 100))
        # Update the display to show the changes
        pygame.display.update()

    def get_selection(self):
        # Main loop to handle events and get the selected option
        while True:
            for event in pygame.event.get():
                # If the user quits the game
                if event.type == pygame.QUIT:
                    return "exit"
                # If the user clicks the mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Check if the user clicked on "Start Game"
                    if 200 < y < 250:
                        # Stop the menu music
                        pygame.mixer.music.stop()
                        return "play"
                    # Check if the user clicked on "Score"
                    elif 300 < y < 350:
                        return "score"
                    # Check if the user clicked on "Exit"
                    elif 400 < y < 450:
                        return "exit"
