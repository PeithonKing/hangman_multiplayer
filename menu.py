import pygame  # noqa: D100
import pygame.gfxdraw
import random
import os

import hangman_chooser  # noqa

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 50

bg = pygame.image.load('bgimg-menu/'+random.choice(os.listdir("bgimg-menu/")))

title_font = pygame.font.SysFont("Arial", 64)
button_font = pygame.font.SysFont("Arial", 32)

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hangman")


class Button:
    """Class for doing everything with a menu button."""

    def __init__(self, x, y, w, h, color1, color2, text):
        """Create the button."""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color1 = color1
        self.color2 = color2
        self.text = text

    def draw(self):
        """Draw a button with text."""
        draw_button(screen, (self.x, self.y, self.w, self.h),
                    self.color1, self.color2)
        text_surface = button_font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.w // 2, self.y + self.h // 2)
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        """Check if the button is clicked."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x <= mouse_x <= self.x + self.w \
            and self.y <= mouse_y <= self.y + self.h


def draw_button(surface, rect, color1, color2):
    """Draw a basic button, no text."""
    colour_rect = pygame.Surface((2, rect[3]))
    pygame.gfxdraw.vline(colour_rect, 0, 0, rect[3], color1)
    pygame.gfxdraw.vline(colour_rect, 1, 0, rect[3], color2)
    colour_rect = pygame.transform.smoothscale(colour_rect, (rect[2], rect[3]))
    surface.blit(colour_rect, rect)


def draw_title(surface):
    """Draw the title in a box."""
    title_surface = title_font.render("Hangman", True, BLACK)
    title_rect = title_surface.get_rect()
    title_rect.center = (screen_width // 2, screen_height // 4)
    pygame.draw.rect(surface, WHITE, title_rect)
    pygame.draw.rect(surface, BLACK, title_rect, 2)
    surface.blit(title_surface, title_rect)


choose_button = Button(250, 300, 300, 50,
                       (50, 50, 255), (255, 192, 203), "Choose a word")
guess_button = Button(250, 400, 300, 50,
                      (200, 200, 0), (0, 128, 0), "Guess a word")

running = True
chooser_running = False
guesser_running = False
while running or chooser_running or guesser_running:
    screen.fill(WHITE)
    if running:
        screen.blit(bg, (0, 0))

        draw_title(screen)
        choose_button.draw()
        guess_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if choose_button.is_clicked():
                    print("Choose a word button clicked")  # PLACEHOLDER
                    running = False
                    chooser_running = True
                    

                if guess_button.is_clicked():
                    print("Guess a word button clicked")  # PLACEHOLDER
                    running = False
                    chooser_running = True
    elif chooser_running:
        hangman_chooser.chooser(screen)


    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
