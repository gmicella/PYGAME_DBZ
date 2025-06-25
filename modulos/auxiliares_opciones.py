import pygame
import modulos.variables as var

def cambiar_fondo_pantalla_opciones():
    fondo_pantalla = pygame.image.load(var.IMAGEN_OPCIONES)
    return fondo_pantalla

def musica_pantalla_opciones(musica_actual):
    if musica_actual != var.MUSICA_OPCIONES:
        pygame.mixer.music.load(var.MUSICA_OPCIONES)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
        return var.MUSICA_OPCIONES
    return musica_actual


def renderizar_texto_opciones(texto: str, fuente: pygame.font, color: dict[tuple], superficie: pygame.Surface, eje_x: int, eje_y: int):
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


def mostrar_encabezado_opciones(titulo_juego: str, textos_opciones: dict, pantalla: pygame.Surface, fuente_titulo: pygame.font.Font, fuente_subtitulo: pygame.font.Font, color: dict[tuple]):
    """
    Muestra el título y subtítulo en las coordenadas especificas.

    Args:
        pantalla: superficie destino
        fuente_titulo: fuente del título
        fuente_subtitulo: fuente del subtítulo
        color: color del texto
    """
    renderizar_texto_opciones(titulo_juego, fuente_titulo, color.get("rojo"), pantalla, 450, 80)      
    renderizar_texto_opciones(textos_opciones.get("titulo pantalla"), fuente_subtitulo, color.get("rojo"), pantalla, 580, 150)       


def mostrar_opciones(pantalla: pygame.Surface, fuente_opciones: pygame.font.Font, textos_opciones: dict, color: dict[tuple]):
    """
    Dibuja cada opción en coordenadas fijas estilo tupla, sin métodos automáticos.

    Args:
        pantalla: superficie destino
        fuente_menu: fuente usada para el texto
        opciones: lista de strings con las opciones
        color: color del texto
    """
    coordenadas = [
        (550, 310),  # MUSICA ON
        (540, 360),  # MUSICA OFF
        (500, 650),  # VOLVER AL MENU
    ]

    lista_opciones = textos_opciones.get("lista opciones")
    color_opcion = color.get("naranja")

    for opcion in range(len(lista_opciones)):
        texto_renderizado = fuente_opciones.render(lista_opciones[opcion], True, color_opcion)
        pantalla.blit(texto_renderizado, coordenadas[opcion])
