import pygame
import modulos.variables as var
import modulos.auxiliares_menu as aux_menu


def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "menu"
    pygame.display.set_caption("MENU")

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if var.RECT_JUGAR.collidepoint(x, y):
                pass
                # retorno = "jugar"
            elif var.RECT_OPCIONES.collidepoint(x, y):                
                retorno = "opciones"
            elif var.RECT_RANKING.collidepoint(x, y):
                pass
                # retorno = "ranking"
            elif var.RECT_SALIR.collidepoint(x, y):
                retorno = "salir"

    return retorno