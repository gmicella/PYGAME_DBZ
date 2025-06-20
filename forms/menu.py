import pygame
import temas.variables as var
import temas.auxiliares as aux


def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "menu"
    pygame.display.set_caption("MENU")

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if var.RECT_START.collidepoint(x, y):
                pass
                # retorno = "jugar"
            elif var.RECT_OPTIONS.collidepoint(x, y):
                pass
                # retorno = "opciones"
            elif var.RECT_RANKING.collidepoint(x, y):
                pass
                # retorno = "ranking"
            elif var.RECT_EXIT.collidepoint(x, y):
                retorno = "salir"

    return retorno