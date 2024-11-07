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
key = pygame.image.load('Images/key.png')
out = pygame.image.load('Images/out.png')

# Sprites Nivel 1
ground1 = pygame.image.load('Images/ground1.png')
wall1 = pygame.image.load('Images/wall1.png')

# Sprites Nivel 2
ground2 = pygame.image.load('Images/ground2.png')
wall2 = pygame.image.load('Images/wall2.png')
"""-------------------------------------------------------
# ESCALADO DE IMÁGENES
-------------------------------------------------------"""
# pygame.transform.scale
robot = pygame.transform.scale(robot,(50,50))
key = pygame.transform.scale(key,(50,50))
out = pygame.transform.scale(out,(50,50))

ground1 = pygame.transform.scale(ground1,(50,50))
wall1 = pygame.transform.scale(wall1,(50,50))

ground2 = pygame.transform.scale(ground2,(50,50))
wall2 = pygame.transform.scale(wall2,(50,50))

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

mapa2 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 1, 1, 1]]

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
    
    global lista_llaves
    
    cell_width = WIDTH // columnas
    cell_height = HEIGHT // filas
    
    # Seleccionar el mapa y las imágenes actuales
    if nivel == 1:
        mapa = mapa1
        current_wall = wall1
        current_ground = ground1
        lista_llaves = llaves_n1
        
    elif nivel == 2:
        mapa = mapa2
        current_wall = wall2
        current_ground = ground2
        lista_llaves = llaves_n2
        
    # Recorrido de listas anidadas para pintar sprites
    for fil in range(len(mapa)):
        for col in range(len(mapa[0])):
            
            if mapa[fil][col] == 0:
                screen.blit(current_ground, (col*cell_width, fil*cell_height))
                
            elif mapa[fil][col] == 1:
                screen.blit(current_wall, (col*cell_width, fil*cell_height))
    
    # Pintar robot en el mapa
    screen.blit(robot, (pos_x*cell_width, pos_y*cell_height))
    
    # Dibujar la salida en la posición adecuada según el nivel
    if nivel == 1:
        screen.blit(out, (salida_x * cell_width, salida_y * cell_height))
    elif nivel == 2:
        screen.blit(out, (salida2_x * cell_width, salida2_y * cell_height))
    
    # Dibujar las llaves generadas
    for llave in lista_llaves:
        screen.blit(key, (llave[1] * cell_width, llave[0] * cell_height))

"""-------------------------------------------------------
# DECLARACIÓN DE VARIABLES GLOBALES
-------------------------------------------------------"""
# Variable de control de inicio/fin del ciclo
running = True

# Definir las posiciones iniciales del robot
pos_x, pos_y = 0,0

# Posición inicial del robot - NIVEL 2
pos2_x, pos2_y = 9, 1

# Nivel actual
nivel = 1

# Posición de salida del laberinto - NIVEL 1
salida_x, salida_y = 9, 9

# Posición de salida del laberinto - NIVEL 2
salida2_x, salida2_y = 0, 6

# Variable global para objetos recolectables
lista_llaves = []

# Usar función que genera las llaves
llaves_n1 = generar_llaves(mapa1)
llaves_n2 = generar_llaves(mapa2)

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
                elif nivel == 2 and pos_y > 0 and mapa2[pos_y-1][pos_x] == 0:
                    pos_y -= 1
            
            # Identificar si se ha presionado la tecla de dirección inferior
            elif event.key == K_DOWN:
                
                if nivel == 1 and pos_y < filas - 1 and mapa1[pos_y+1][pos_x] == 0:
                    pos_y += 1
                elif nivel == 2 and pos_y < filas - 1 and mapa2[pos_y+1][pos_x] == 0:
                    pos_y += 1
                
            elif event.key == K_LEFT:
                
                if nivel == 1 and pos_x > 0 and mapa1[pos_y][pos_x-1] == 0:
                    pos_x -= 1
                elif nivel == 2 and pos_x > 0 and mapa2[pos_y][pos_x-1] == 0:
                    pos_x -= 1
            
            elif event.key == K_RIGHT:
                
                if nivel == 1 and pos_x < columnas - 1 and mapa1[pos_y][pos_x+1] == 0:
                    pos_x += 1
                elif nivel == 2 and pos_x < columnas - 1 and mapa2[pos_y][pos_x+1] == 0:
                    pos_x += 1
                
    # Verifica si el robot ha recolectado un objeto
    for pos_llave in lista_llaves[:]:
        if pos_y == pos_llave[0] and pos_x == pos_llave[1]:
            lista_llaves.remove(pos_llave)
            llaves_recolectadas += 1
    
    # Verifica si el robot ha llegado a la posición de salida del nivel 1
    if nivel == 1 and pos_x == salida_x and pos_y == salida_y and llaves_recolectadas == 2:
        nivel = 2
        pos_x, pos_y = pos2_x, pos2_y  # Cambiar la posición del robot al inicio del nivel 2
        llaves_recolectadas = 0       # Reiniciar el conteo de objetos recolectados
    
    # Llamar a la función de dibujo
    map_draw()
    
    # Actualizar ventana
    pygame.display.flip()
    
# Cerrar Pygame
pygame.quit()