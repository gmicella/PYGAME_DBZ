import pygame
pygame.init()
pygame.mixer.init()

from modulos.juego import jugar_dragon_ball

if __name__ == "__main__":
    jugar_dragon_ball()