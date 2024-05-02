import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mover Círculo en Cuadrado en Pygame")

# Colores (en formato RGB)
white = (255, 255, 255)
blue = (0, 0, 255)

# Coordenadas y tamaño del cuadrado
square_x = 300
square_y = 200
square_size = 200

# Coordenadas del centro del círculo
circle_x = square_x + square_size // 2
circle_y = square_y + square_size // 2
circle_radius = 20

# Velocidad de movimiento del círculo
circle_speed = 0.2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Mover el círculo en respuesta a las teclas presionadas
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Dibujar el fondo blanco
    screen.fill(white)

    # Dibujar un cuadrado azul
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))

    # Dibujar un círculo en el centro del cuadrado
    pygame.draw.circle(screen, white, (circle_x, circle_y), circle_radius - 10)

    # Actualizar la pantalla
    pygame.display.flip()
