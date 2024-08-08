"""-------------------------------------------------------
  IMPORACIÓN DE LIBRERÍAS
-------------------------------------------------------"""
import pygame
from pygame.locals import *
pygame.init()

"""--------------------------------------------------
  CONFIGURACIÓN DE VENTANA
--------------------------------------------------"""
# Definir tamaño de ventana
WIDTH, HEIGHT = 500, 500

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Definir título de ventana
pygame.display.set_caption("JUEGO DE LABERINTOS |ROBOMAZE|")

"""--------------------------------------------------
  INICIALIZACIÓN DE PARÁMETROS PYGAME
--------------------------------------------------"""
# Inicializar Pygame
pygame.init()

# Inicializar fuentes de texto
pygame.font.init()
fuente = pygame.font.SysFont('Roboto', 35)

"""-------------------------------------------------------
  CARGA DE SPRITES
-------------------------------------------------------"""
# pygame.image.load('Images/robot.png')
robot = pygame.image.load('Images/robot.png')
"""-------------------------------------------------------
# ESCALADO DE IMÁGENES
-------------------------------------------------------"""
# pygame.transform.scale

"""--------------------------------------------------
DEFINICIÓN DE MAPAS
--------------------------------------------------"""
# Cantidad de columnas y filas
columnas, filas = 10, 10

"""-------------------------------------------------
FUNCIÓN DE DIBUJO PRINCIPAL
-------------------------------------------------"""
def map_draw():
    pass

"""-------------------------------------------------------
# DECLARACIÓN DE VARIABLES GLOBALES
-------------------------------------------------------"""
# Variable de control de inicio/fin del ciclo
running = True

"""-------------------------------------------------
CICLO PRINCIPAL DEL PROGRAMA
-------------------------------------------------"""
while running:
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    
    # Actualizar ventana
    pygame.display.flip()
    
# Cerrar Pygame
pygame.quit()