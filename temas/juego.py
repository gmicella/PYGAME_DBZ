import pygame
import forms.menu as menu
import variables as var
import auxiliares as aux


def jugar_dragon_ball():

    # Crea la ventana del juego con las dimensiones y el título.
    pantalla = pygame.display.set_mode(var.DIMENSION_PANTALLA)
    pygame.display.set_caption(var.TITULO_JUEGO)

    fondo_original = pygame.image.load(var.IMAGEN_MENU)
    fondo_menu = pygame.transform.scale(fondo_original, var.DIMENSION_PANTALLA)

    pygame.mixer.music.load(var.MUSICA_MENU)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

    fuente_titulo = pygame.font.Font(var.FUENTE_TITULO_JUEGO, 55)
    fuente_menu = pygame.font.Font(var.FUENTE_TITULO_JUEGO, 45)
    fuente_opciones = pygame.font.Font(var.FUENTE_TITULO_JUEGO, 40)

    # Crea un reloj interno, para controlar el ritmo del juego (cuántas veces por segundo se repite el bucle principal).
    reloj = pygame.time.Clock()

    ejecutando = True

    form_actual = "menu"
    bandera_juego = False

    while ejecutando:
        
        # ================================= 1) GESTIÓN DE EVENTOS ============================================================================
        
        cola_eventos = pygame.event.get()
        reloj.tick(var.FPS)

        if form_actual == "menu":
            form_actual = menu.mostrar_menu(pantalla, cola_eventos)


        elif form_actual == "salir":
            ejecutando = False

        # ================================= 2) ACTUALIZACIÓN DE LÓGICA DEL JUEG0 =============================================================



        # ================================= 3) DIBUJO EN PANTALLA ===========================================================================

        pantalla.blit(fondo_menu, (0, 0))

        aux.mostrar_encabezado(var.TITULO_JUEGO, var.TEXTOS_MENU_PRINCIPAL, pantalla, fuente_titulo, fuente_menu, var.colores)
        aux.mostrar_opciones_juego(pantalla, fuente_opciones, var.TEXTOS_MENU_PRINCIPAL, var.colores)


        # ================================= 4) ACTUALIZACIÓN DE LA PANTALLA =================================================================
        pygame.display.flip()

        # ================================= 5) CONTROL DE VELOCIDAD EN FPS ==================================================================
        

    # Cierra todos los módulos activos de Pygame y libera recursos (termina correctamente el programa).
    pygame.quit()