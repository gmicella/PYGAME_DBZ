import pygame
import modulos.formularios.form_base as form_base
from utn_fra.pygame_widgets import (
    Button, Label
)
import modulos.variables as var
import modulos.auxiliares_menu as aux_menu


def inicializar_form_menu_principal(nombre: str, pantalla: pygame.Surface, activo: bool, coords: tuple[int, int], numero_nivel: int, ruta_musica: str, ruta_imagen_fondo: str):
    formulario = form_base.crear_form_base(nombre, pantalla, activo, coords, numero_nivel, ruta_musica, ruta_imagen_fondo)

    formulario["boton_jugar"] = Button(x=590, y=350, text="Jugar", screen=form_base.get("pantalla_principal"), font_path=var.FUENTE_TITULO_JUEGO, color=var.COLOR_ROJO, font_size=40, on_click=None, on_click_param=None)
    formulario["boton_opciones"] = Button(x=570, y=420, text="Opciones", screen=form_base.get("pantalla_principal"), font_path=var.FUENTE_TITULO_JUEGO, color=var.COLOR_ROJO, font_size=40, on_click=None, on_click_param=None)
    formulario["boton_ranking"] = Button(x=580, y=490, text="Ranking", screen=form_base.get("pantalla_principal"), font_path=var.FUENTE_TITULO_JUEGO, color=var.COLOR_ROJO, font_size=40, on_click=None, on_click_param=None)
    formulario["boton_salir"] = Button(x=600, y=560, text="Salir", screen=form_base.get("pantalla_principal"), font_path=var.FUENTE_TITULO_JUEGO, color=var.COLOR_ROJO, font_size=40, on_click=None, on_click_param=None)
    formulario["lista_botones"] = [
        formulario.get("boton_jugar"), formulario.get("boton_opciones"), formulario.get("boton_ranking"), formulario.get("boton_salir"),  
    ]


# def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
#     retorno = "menu"
#     pygame.display.set_caption("MENU")

#     for evento in cola_eventos:
#         if evento.type == pygame.QUIT:
#             retorno = "salir"
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             x, y = evento.pos
#             if var.RECT_JUGAR.collidepoint(x, y):
#                 pass
#                 # retorno = "jugar"
#             elif var.RECT_OPCIONES.collidepoint(x, y):                
#                 retorno = "opciones"
#             elif var.RECT_RANKING.collidepoint(x, y):
#                 pass
#                 # retorno = "ranking"
#             elif var.RECT_SALIR.collidepoint(x, y):
#                 retorno = "salir"

#     return retorno