import pygame

DIMENSION_PANTALLA = (1280, 720)
TITULO_JUEGO = "DRAGON BALL Z TCG"
TEXTOS_MENU_PRINCIPAL = {
    "titulo pantalla": "MENU PRINCIPAL",
    "lista opciones": ["START", "OPTIONS", "RANKING", "EXIT"]
}

#RECTANGULOS OPCIONES MENU
RECT_START = pygame.Rect(590, 350, 200, 40)
RECT_OPTIONS = pygame.Rect(570, 420, 200, 40)
RECT_RANKING = pygame.Rect(570, 490, 200, 40)
RECT_EXIT = pygame.Rect(600, 560, 200, 40) 


FPS = 60
FUENTE_TITULO_JUEGO = "assets_Dragon_Ball_Trading_Card_Game/fonts/Saiyan-Sans.ttf"
MUSICA_MENU = "assets_Dragon_Ball_Trading_Card_Game/audio/music/form_main_menu.ogg"
IMAGEN_MENU = "assets_Dragon_Ball_Trading_Card_Game/img/forms/img_5.png"

colores = {
    "blanco": (255, 255, 255),
    "negro": (0, 0, 0),
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0),
    "celeste": (0, 255, 255),
    "violeta": (128, 0, 128),
    "gris": (128, 128, 128),
    "naranja": (255, 165, 0)
}