"""-------------------------------------------------------
  IMPORACIÓN DE LIBRERÍAS
-------------------------------------------------------"""
import pygame
from pygame.locals import *
import random

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
ground1 = pygame.image.load('Images/ground1.png')
wall1 = pygame.image.load('Images/wall1.png')
key = pygame.image.load('Images/key.png')
out = pygame.image.load('Images/out.png')

"""-------------------------------------------------------
# ESCALADO DE IMÁGENES
-------------------------------------------------------"""
# pygame.transform.scale
robot = pygame.transform.scale(robot,(50,50))
ground1 = pygame.transform.scale(ground1,(50,50))
wall1 = pygame.transform.scale(wall1,(50,50))
key = pygame.transform.scale(key,(50,50))
out = pygame.transform.scale(out,(50,50))

"""--------------------------------------------------
DEFINICIÓN DE MAPAS
--------------------------------------------------"""
# Cantidad de columnas y filas
columnas, filas = 10, 10

mapa1 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

"""--------------------------------------------------
FUNCIÓN QUE GENERA LAS LLAVES ALEATORIAS
--------------------------------------------------"""
# Generar llaves aleatorias en el mapa
def generar_llaves(mapa):
    
    lista_llaves = []
     
    for i in range(2):
        
        while True:
            rand_fil, rand_col = random.randint(0, filas - 1), random.randint(0, columnas - 1)
            if mapa[rand_fil][rand_col] == 0 and [rand_fil, rand_col] not in lista_llaves and not (rand_fil == 0 and rand_col == 0):
                lista_llaves.append([rand_fil, rand_col])
                break
            
    return lista_llaves

"""-------------------------------------------------
FUNCIÓN DE DIBUJO PRINCIPAL
-------------------------------------------------"""
def map_draw():
    
    global llaves_n1
    
    cell_width = WIDTH // columnas
    cell_height = HEIGHT // filas
    
    # Recorrido de listas anidadas para pintar sprites
    for fil in range(len(mapa1)):
        for col in range(len(mapa1[0])):
            
            if mapa1[fil][col] == 0:
                screen.blit(ground1, (col*cell_width, fil*cell_height))
                
            elif mapa1[fil][col] == 1:
                screen.blit(wall1, (col*cell_width, fil*cell_height))
    
    # Pintar robot en el mapa
    screen.blit(robot, (pos_x*cell_width, pos_y*cell_height))
    
    # Pintar salida del primer nivel
    screen.blit(out, (salida_x * cell_width, salida_y * cell_height))
    
    # Dibujar las llaves generadas
    for llave in llaves_n1:
        screen.blit(key, (llave[1] * cell_width, llave[0] * cell_height))

    pass

"""-------------------------------------------------------
# DECLARACIÓN DE VARIABLES GLOBALES
-------------------------------------------------------"""
# Variable de control de inicio/fin del ciclo
running = True

# Definir las posiciones iniciales del robot
pos_x, pos_y = 0,0

# Nivel actual
nivel = 1

# Posición de salida del laberinto - NIVEL 1
salida_x, salida_y = 9, 9

# Usar función que genera las llaves para el nivel 1
llaves_n1 = generar_llaves(mapa1)

# Contador de llaves recolectadas
llaves_recolectadas = 0

"""-------------------------------------------------
CICLO PRINCIPAL DEL PROGRAMA
-------------------------------------------------"""
while running:
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        
        # Identificar si se ha presionado una tecla
        elif event.type == KEYDOWN:
            
            # Identificar si se ha presionado la tecla de dirección superior
            if event.key == K_UP:
                
                if nivel == 1 and pos_y > 0 and mapa1[pos_y-1][pos_x] == 0:
                    pos_y -= 1
            
            # Identificar si se ha presionado la tecla de dirección inferior
            elif event.key == K_DOWN:
                
                if nivel == 1 and pos_y < filas - 1 and mapa1[pos_y+1][pos_x] == 0:
                    pos_y += 1
                
            elif event.key == K_LEFT:
                
                if nivel == 1 and pos_x > 0 and mapa1[pos_y][pos_x-1] == 0:
                    pos_x -= 1
            
            elif event.key == K_RIGHT:
                
                if nivel == 1 and pos_x < columnas - 1 and mapa1[pos_y][pos_x+1] == 0:
                    pos_x += 1
                
    # Verifica si el robot ha recolectado un objeto
    for llave in llaves_n1[:]:
        if pos_y == llave[0] and pos_x == llave[1]:
            llaves_n1.remove(llave)
            llaves_recolectadas += 1
                
    # Llamar a la función de dibujo
    map_draw()
    
    # Actualizar ventana
    pygame.display.flip()
    
# Cerrar Pygame
pygame.quit()