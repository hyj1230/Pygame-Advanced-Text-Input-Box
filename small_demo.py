import pygame
import sys
import os
from INS_text_input import TextInput


os.environ["SDL_IME_SHOW_UI"] = "1"

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.key.set_repeat(450, 25)

clock = pygame.time.Clock()

input_box = TextInput(screen_rect=screen.get_rect(),
                      font=pygame.font.Font('CHSansSC.ttf', 16),
                      font_size=16, font_color=(0, 0, 0), line_height=24,
                      rect=pygame.Rect(10, 10, 780, 580),
                      init_text='Hello, World\nThis is a text input box', multi_lines=True)

while True:
    pygame_events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (221, 221, 221), input_box.rect.inflate(4, 4), width=2)
    input_box.handle_events(pygame_events, mouse_pos)
    input_box.display(screen, mouse_pos)

    pygame.display.update()
    clock.tick(114514)
