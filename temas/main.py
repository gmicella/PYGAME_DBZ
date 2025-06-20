import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from juego import jugar_dragon_ball

pygame.init()

jugar_dragon_ball()