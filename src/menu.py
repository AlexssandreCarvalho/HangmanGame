import pygame


class Menu:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/menu_music.mp3")
        pygame.mixer.music.play(-1)
        self.WIDTH, self.HEIGHT = 800, 500
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.options = ["Start Game", "Score", "Exit"]
        self.TITLE_FONT = pygame.font.SysFont("comicsans", 70)
        self.FONT = pygame.font.SysFont("comicsans", 40)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.background = pygame.image.load("assets/images/menu_background.png")

    def draw(self):
        self.win.blit(self.background, (0, 0))
        # Desenhar o título "HANGMAN (Demo)"
        text = self.TITLE_FONT.render("HANGMAN (Demo)", 1, self.BLACK)
        self.win.blit(text, (self.WIDTH / 2 - text.get_width() / 2, 20))
        for i, option in enumerate(self.options):
            text = self.FONT.render(option, 1, self.BLACK)
            self.win.blit(text, (self.WIDTH / 2 - text.get_width() / 2, 200 + i * 100))
        pygame.display.update()

    def get_selection(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 200 < y < 250:
                        pygame.mixer.music.stop()
                        return "play"
                    elif 300 < y < 350:
                        return "score"
                    elif 400 < y < 450:
                        return "exit"
