import pygame
import modulos.variables as var

def crear_form_base(nombre: str, pantalla: pygame.Surface, activo: bool, coords: tuple[int, int], numero_nivel: int, ruta_musica: str, ruta_imagen_fondo: str) -> dict:
    formulario = {}
    formulario["nombre"] = nombre
    formulario["pantalla_principal"] = pantalla
    formulario["activo"] = activo
    formulario["coord_x"] = coords[0]
    formulario["coord_y"] = coords[1]
    formulario["numero_nivel"] = numero_nivel
    formulario["ruta_musica"] = ruta_musica
    formulario["imagen_fondo"] = pygame.image.load(ruta_imagen_fondo)
    formulario["imagen_fondo"] = pygame.transform.scale(formulario.get("imagen_fondo"), var.DIMENSION_PANTALLA)
    formulario["rectangulo"] = formulario.get("imagen_fondo").get_rect()
    formulario["rectangulo"].x = coords[0]
    formulario["rectangulo"].y = coords[1]
    return formulario

# https://youtu.be/kf_QPLLrAQI?t=2429