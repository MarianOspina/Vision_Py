import pygame
import cv2
import numpy as np
import mediapipe as mp

width, height = 800, 600
# Definir el color del círculo (en formato RGB)
circle_color = (255, 0, 0)  # Rojo

# Coordenadas del centro del círculo
circle_center = (width // 2, height // 2)

# Radio del círculo
circle_radius = 10


# Librerías de dibujado y detección de MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Parámetros del círculo a dibujar
circle_radius = 5
circle_color = (0, 255, 0)


# Inicializar Pygame
pygame.init()

# Configuración de la pantalla de Pygame
screen_width, screen_height = 800, 600
camera_width, camera_height = 250, 150

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cámara en Pygame")

# Inicializar la cámara de OpenCV
cap = cv2.VideoCapture(0)

font = pygame.font.Font(None, 18)  # Puedes ajustar el tamaño de la fuente aquí

with mp_face_mesh.FaceMesh(
        min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()  # Liberar la cámara
                cv2.destroyAllWindows()  # Cerrar las ventanas de OpenCV
                exit()

        # Capturar un frame de la cámara
        success, frame = cap.read()

        # Verificar que haya frame disponible
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Invertir horizontalmente el frame para que la imagen no esté espejada
        frame = cv2.flip(frame, 1)

        # Escalar el frame a las dimensiones deseadas (200x150)
        frame = cv2.resize(frame, (camera_width, camera_height))

        # Convertir el frame de OpenCV a un formato adecuado para Pygame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detectar cara
        results = face_mesh.process(frame)

        # Obtener coordenadas de punto de referencia
        x, y = 0, 0

        # Verificar que se haya detectado una cara
        if results.multi_face_landmarks:
            # Tomar el primer rostro
            face_landmarks = results.multi_face_landmarks[0]

            # Obtener punto de referencia deseado
            # Ej: Punta de nariz
            x = int(face_landmarks.landmark[4].x * frame.shape[1])
            y = int(face_landmarks.landmark[4].y * frame.shape[0])

        # Dibujar círculo en coordenadas deseadas
        frame = cv2.circle(frame, (x, y), circle_radius, circle_color, -1)
        # Voltear horizontalmente para sincronizar
        frame = cv2.flip(frame, 1)

        pygame_frame = pygame.surfarray.make_surface(np.rot90(frame))

        # Rellenar la pantalla de blanco
        screen.fill((255, 255, 255))
        # Dibujar el frame escalado en la esquina superior izquierda
        screen.blit(pygame_frame, (0, 0))


        pygame.display.update()
