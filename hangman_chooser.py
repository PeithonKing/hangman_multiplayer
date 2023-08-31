import pygame  # noqa: D100
import sys
import requests

pygame.init()

text = ""


def check_word(word: str):
    """Check if the word is valid for use in hangman."""
    with open("wordlist.txt") as wordfile:
        return word.lower() in [x.strip() for x in wordfile.readlines()]


def chooser(screen):
    """Open the word chooser window."""
    global text

    font = pygame.font.Font(None, 90)
    color = pygame.Color("lightskyblue3")
    input_box = pygame.Rect(100, 275, 700, 70)
    title_font = pygame.font.Font(None, 48)
    button_font = pygame.font.Font(None, 36)
    button_box = pygame.Rect(300, 375, 200, 50)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_box.collidepoint(event.pos):
                print(text)
                text = ""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if check_word(text):
                    requests.get(f'/start_game/{text}')
                text = ""
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if len(text) < 10:
                    text += event.unicode

    screen.fill((255, 255, 255))

    title_surface = title_font.render("Choose a word", True, (0, 0, 0))
    title_x = (800 - title_surface.get_width()) // 2
    screen.blit(title_surface, (title_x, 200))

    txt_surface = font.render(text, True, color)

    width = max(600, txt_surface.get_width() + 10)
    input_box.w = width

    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    button_surface = button_font.render("Choose", True, (0, 0, 0))
    button_text_x = button_box.x + \
        (button_box.width - button_surface.get_width()) // 2
    button_text_y = button_box.y + \
        (button_box.height - button_surface.get_height()) // 2
    screen.blit(button_surface, (button_text_x, button_text_y))

    pygame.draw.rect(screen, color, input_box, 2)

    pygame.draw.rect(screen, (0, 0, 0), button_box, 2)
