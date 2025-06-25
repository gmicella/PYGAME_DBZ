import pygame

DIMENSION_PANTALLA = (1280, 720)
TITULO_JUEGO = "DRAGON BALL Z TCG"
TEXTOS_MENU_PRINCIPAL = {
    "titulo pantalla": "MENU PRINCIPAL",
    "lista opciones": ["JUGAR", "OPCIONES", "RANKING", "SALIR"]
}
TEXTOS_OPCIONES = {
    "titulo pantalla": "OPCIONES",
    "lista opciones": ["MUSICA ON", "MUSICA OFF", "VOLVER AL MENU"]
}

#RECTANGULOS OPCIONES MENU
RECT_JUGAR = pygame.Rect(590, 350, 200, 40)
RECT_OPCIONES = pygame.Rect(570, 420, 200, 40)
RECT_RANKING = pygame.Rect(580, 490, 200, 40)
RECT_SALIR = pygame.Rect(600, 560, 200, 40) 


FPS = 60
FUENTE_TITULO_JUEGO = "assets_Dragon_Ball_Trading_Card_Game/fonts/Saiyan-Sans.ttf"

MUSICA_MENU = "assets_Dragon_Ball_Trading_Card_Game/audio/music/form_main_menu.ogg"
MUSICA_OPCIONES = "assets_Dragon_Ball_Trading_Card_Game/audio/music/form_options.ogg"

IMAGEN_MENU = "assets_Dragon_Ball_Trading_Card_Game/img/forms/img_5.png"
IMAGEN_OPCIONES = "assets_Dragon_Ball_Trading_Card_Game/img/forms/img_6.png"

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

# COLORES
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_AMARILLO = (255, 255, 0)
COLOR_CELESTE = (0, 255, 255)
COLOR_VIOLETA = (128, 0, 128)
COLOR_GRIS = (128, 128, 128)
COLOR_NARANJA = (255, 165, 0)