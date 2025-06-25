import pygame


def renderizar_texto(texto: str, fuente: pygame.font, color: dict[tuple], superficie: pygame.Surface, eje_x: int, eje_y: int):
    """
    Renderiza el texto en coordenadas fijas (eje_x, eje_y).

    Args:
        texto: texto a mostrar
        fuente: fuente 
        color: color del texto
        superficie: superficie destino
        eje_x: coordenada de eje_x 
        eje_y: coordenada de eje_y 
    """
    render = fuente.render(texto, True, color)
    superficie.blit(render, (eje_x, eje_y))


def mostrar_encabezado(titulo_juego: str, textos_menu: dict, pantalla: pygame.Surface, fuente_titulo: pygame.font.Font, fuente_subtitulo: pygame.font.Font, color: dict[tuple]):
    """
    Muestra el título y subtítulo en las coordenadas especificas.

    Args:
        pantalla: superficie destino
        fuente_titulo: fuente del título
        fuente_subtitulo: fuente del subtítulo
        color: color del texto
    """
    renderizar_texto(titulo_juego, fuente_titulo, color.get("rojo"), pantalla, 420, 80)      
    renderizar_texto(textos_menu.get("titulo pantalla"), fuente_subtitulo, color.get("rojo"), pantalla, 520, 150)       


def mostrar_opciones_juego(pantalla: pygame.Surface, fuente_opciones: pygame.font.Font, textos_menu: dict, color: dict[tuple]):
    """
    Dibuja cada opción en coordenadas fijas estilo tupla, sin métodos automáticos.

    Args:
        pantalla: superficie destino
        fuente_menu: fuente usada para el texto
        opciones: lista de strings con las opciones
        color: color del texto
    """
    coordenadas = [
        (590, 350),  # JUGAR 
        (570, 420),  # OPCIONES 
        (580, 490),  # RANKING 
        (600, 560)   # SALIR 
    ]

    lista_opciones = textos_menu.get("lista opciones")
    color_opcion = color.get("naranja")

    for opcion in range(len(lista_opciones)):
        texto_renderizado = fuente_opciones.render(lista_opciones[opcion], True, color_opcion)
        pantalla.blit(texto_renderizado, coordenadas[opcion])






# import pygame
# import variables as var

# pygame.init()


# def crear_y_mostrar_boton_texto(pantalla: pygame.Surface, fuente: str, texto: str, color: tuple, dimension: int, x_centro: int, y_centro:int) -> None:
#     '''
#     '''
#     boton = crear_boton_texto(fuente, texto, color, dimension, x_centro, y_centro)
#     mostrar_boton_texto(pantalla, boton)


# def crear_boton_texto(fuente: str, texto: str, color: tuple, dimension: int, x_centro: int, y_centro: int) -> dict:
#     '''
#     '''
#     fuente = pygame.font.Font(fuente, dimension)
#     superficie = fuente.render(texto, True, color)
#     rectangulo = superficie.get_rect()
#     rectangulo.center = (x_centro, y_centro)
#     boton = {
#         "texto": texto,
#         "fuente": fuente,
#         "color": color,
#         "superficie": superficie,
#         "rectangulo": rectangulo
#     }
#     return boton

# def mostrar_boton_texto(pantalla: pygame.Surface, boton: dict) -> None:
#     '''
#     '''
#     superficie = boton.get("superficie")
#     rectangulo = boton.get("rectangulo")
#     pantalla.blit(superficie, rectangulo)


# def mostrar_texto(pantalla: pygame.Surface, fuente: str, texto: str, color: tuple, dimension: int, x_centro: int, y_centro:int) -> None:
#     '''
#     '''
#     tipo_letra = pygame.font.Font(fuente, dimension)
#     superficie = tipo_letra.render(texto, True, color)
#     rectangulo = superficie.get_rect()
#     rectangulo.center = (x_centro, y_centro)
#     pantalla.blit(superficie, rectangulo)
