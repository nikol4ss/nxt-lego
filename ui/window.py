import pygame

def init_window(size, title):
    pygame.init()
    pygame.display.set_mode(size)
    pygame.display.set_caption(title)
