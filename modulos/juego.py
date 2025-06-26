import pygame
import sys
import formularios.form_manager as form_manager
import modulos.formularios.menu as menu
import modulos.formularios.opciones as opciones
import modulos.variables as var
import modulos.auxiliares_menu as aux_menu
import modulos.auxiliares_opciones as aux_opciones


def jugar_dragon_ball():

    pygame.init()

    pantalla = pygame.display.set_mode(var.DIMENSION_PANTALLA)
    pygame.display.set_caption(var.TITULO_JUEGO)
    ejecutando = True
    reloj = pygame.time.Clock()
    datos_juego = {
        "puntaje": 0,
        "nombre": "PLAYER",
        "volumen_musica": 100,
        "tiempo_finalizado": None
    }

    imagen_fondo = pygame.image.load(var.IMAGEN_MENU)
    imagen_fondo = pygame.transform.scale(imagen_fondo, var.DIMENSION_PANTALLA)

    musica_actual = var.MUSICA_MENU
    pygame.mixer.music.load(musica_actual)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

    fuente_titulo = pygame.font.Font(var.FUENTE_TITULO_JUEGO, 55)
    fuente_menu = pygame.font.Font(var.FUENTE_TITULO_JUEGO, 45)
    fuente_opciones = pygame.font.Font(var.FUENTE_TITULO_JUEGO, 40)

    form_actual = "menu"
    bandera_juego = False


    forms = form_manager.crear_form_manager(pantalla, datos_juego)

    while ejecutando:
                
        cola_eventos = pygame.event.get()
        
        for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                ejcutando = False


        reloj.tick(var.FPS)
        pantalla.blit(imagen_fondo, (0, 0))

        if form_actual == "menu":
            aux_menu.mostrar_encabezado(var.TITULO_JUEGO, var.TEXTOS_MENU_PRINCIPAL, pantalla, fuente_titulo, fuente_menu, var.colores)
            aux_menu.mostrar_opciones_juego(pantalla, fuente_opciones, var.TEXTOS_MENU_PRINCIPAL, var.colores)
            form_actual = menu.mostrar_menu(pantalla, cola_eventos)

        elif form_actual == "opciones":
            imagen_fondo = aux_opciones.cambiar_fondo_pantalla_opciones()
            aux_opciones.mostrar_encabezado_opciones(var.TITULO_JUEGO, var.TEXTOS_OPCIONES, pantalla, fuente_titulo, fuente_menu, var.colores)
            aux_opciones.mostrar_opciones(pantalla, fuente_opciones, var.TEXTOS_OPCIONES, var.colores)
            musica_actual = aux_opciones.musica_pantalla_opciones(musica_actual)
            form_actual = opciones.mostrar_opciones(pantalla, cola_eventos)



        elif form_actual == "salir":
            ejecutando = False

        # ================================= 2) ACTUALIZACIÓN DE LÓGICA DEL JUEG0 =============================================================

        # ================================= 3) DIBUJO EN PANTALLA ===========================================================================

        # ================================= 4) ACTUALIZACIÓN DE LA PANTALLA =================================================================
        pygame.display.flip()


    # Cierra todos los módulos activos de Pygame y libera recursos (termina correctamente el programa).
    pygame.quit()
    sys.exit()