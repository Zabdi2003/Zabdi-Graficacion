import numpy as np
import cv2

# Función para generar un punto de la rosa en función del parámetro t
def generar_punto_rosa(a, k, t):
    r = a * np.cos(k * t)  # Radio en función de t
    x = int(r * np.cos(t) + 300)  # Desplazamiento para centrar
    y = int(r * np.sin(t) + 300)
    return (x, y)

# Dimensiones de la imagen
img_width, img_height = 600, 600

# Crear una imagen en blanco
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Parámetros de la rosa
a = 200  # Amplitud (tamaño de la rosa)
k = 5    # Número de pétalos
num_puntos = 1000

# Crear los valores del parámetro t para la animación
t_vals = np.linspace(0, 2 * np.pi, num_puntos)

# Bucle de animación para dibujar la rosa
for t in t_vals:
    # Generar el punto en la rosa
    punto = generar_punto_rosa(a, k, t)
    
    # Dibujar el punto en la rosa
    cv2.circle(imagen, punto, radius=1, color=(0, 255, 0), thickness=-1)
    
    # Mostrar la imagen con el punto en movimiento
    cv2.imshow('Rosa', imagen)
    
    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(5)

# Bucle de animación para rotar la rosa
angle = 0
while True:
    # Obtener la matriz de rotación
    M = cv2.getRotationMatrix2D((img_width // 2, img_height // 2), angle, 1)
    
    # Aplicar la rotación a la imagen
    imagen = cv2.warpAffine(imagen, M, (img_width, img_height))
    
    # Mostrar la imagen rotada
    cv2.imshow('Rosa', imagen)
    
    # Incrementar el ángulo de rotación
    angle += 1
    if angle >= 360:
        angle = 0
    
    # Controlar la velocidad de la rotación (en milisegundos)
    if cv2.waitKey(50
                   ) & 0xFF == 27:  # Presionar 'Esc' para salir
        break

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()